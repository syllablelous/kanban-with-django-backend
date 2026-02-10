<script>
    import TaskCard from './TaskCard.vue';

    export default {
        name: "StatusListCard",
        props: {
            status: {
                type: String,
                required: true,
            },
            tasks: {
                type: Array,
                required: true
            },
        },
        computed: {
            filteredTasks() {
                return this.tasks.filter(task => task.status === this.status)
            },
            statusClass() {
                return `status-${this.status.toLowerCase()}`
            },
            statusColor() {
                const colors = {
                    pending: '#EECC75',
                    in_progress: '#BAC0FF',
                    completed: '#75EDBF',
                    cancelled: '#EF7275'
                }

                return colors[this.status.toLowerCase()]
            },
            formattedStatus() {
                return this.status
                    .toLowerCase()
                    .split('_')
                    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                    .join(' ')
            }
        },
        components: {
            TaskCard,
        },
        methods: {
            onDrop(event) {
                const taskId = Number(event.dataTransfer.getData('taskId'))
                this.$emit('task-dropped', {
                    taskId,
                    newStatus: this.status
                })
            }
        }
    };
</script>

<template>
    <section 
        class="status-list-card" 
        :class="statusClass"
        @dragover.prevent
        @drop="onDrop"
    >
        <h1>{{ formattedStatus }} Tasks</h1>
        <TaskCard
            v-for="task in filteredTasks"
            :key="task.id"
            :task="task"
            :base-color="statusColor"
            @edit="task => $emit('edit-task', task)"
            @delete="id => $emit('delete-task', id)"
        />

        <p v-if="filteredTasks.length === 0" class="empty-text">
            No tasks here
        </p>
    </section>
</template>

<style scoped>
    .status-list-card {
        flex: 1 1 calc(25% - 16px);
        padding: 15px;
        box-sizing: border-box;
        border-radius: 8px;
        /* align-items: center; */
        text-align: left;
    }

    .status-list-card.status-pending {
        background-color: #EECC75;
    }

    .status-list-card.status-in_progress {
        background-color: #BAC0FF;
    }

    .status-list-card.status-completed {
        background-color: #75EDBF;
    }

    .status-list-card.status-cancelled {
        background-color: #EF7275;
    }

    .status-list-card h1 {
        /* text-align: left; */
        font-size: 22px;
        margin-bottom: 10px;
    }

    .empty-text {
        font-size: 14px;
        color: #2c3e50;
        opacity: 0.7;
        margin-top: 10px;
    }

    @media (max-width: 900px) {
        .status-list-card {
            flex: 1 1 calc(50% - 16px);
        }
    }

    @media (max-width: 500px) {
        .status-list-card {
            flex: 1 1 100%;
        }
    }
</style>