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
        data() {
            return {
                isDragOver: false
            }
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
                const labels = {
                    PENDING: 'Pending',
                    IN_PROGRESS: 'In Progress',
                    COMPLETED: 'Completed',
                    CANCELLED: 'Cancelled'
                }

                return labels[this.status] || this.status
            }
        },
        components: {
            TaskCard,
        },
        methods: {
            onDrop(event) {
                const taskId = Number(event.dataTransfer.getData('taskId'))
                this.isDragOver = false

                this.$emit('task-dropped', {
                    taskId,
                    newStatus: this.status
                })
            }
        },
    };
</script>

<template>
    <section 
        class="status-list-card" 
        :class="[statusClass, { 'drag-over': isDragOver }]"
        @dragover.prevent="isDragOver = true"
        @dragleave="isDragOver = false"
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
        text-align: left;
        position: relative;
        transition: box-shadow 0.2s ease;
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
        font-size: 22px;
        margin-bottom: 10px;
    }
    
    .status-list-card.drag-over::after {
        content: '';
        position: absolute;
        inset: 0;
        background-color: rgba(79, 70, 229, 0.18);
        border-radius: inherit;
        pointer-events: none;
    }
    
    .status-list-card.drag-over {
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.6);
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