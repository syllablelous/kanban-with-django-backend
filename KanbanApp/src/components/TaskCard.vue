<script>
    export default {
        name: "TaskCard",
        props: {
            task: {
                type: Object,
                required: true,
            },
            baseColor: {
                type: String,
                required: true,
            }
        },
        emits: ['edit', 'delete'],
        computed: {
            formattedDueDate() {
                if (!this.task.due_date) return ''

                const date = new Date(this.task.due_date)

                return date.toLocaleString('en-PH', {
                    year: 'numeric',
                    month: 'short',
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit',
                    hour12: true,
                    timeZone: 'Asia/Manila',
                })
            },
        },
        methods: {
            onDragStart(event) {
                event.dataTransfer.setData('taskId', this.task.id)
                event.target.classList.add('dragging')
            },
            onDragEnd(event) {
                event.target.classList.remove('dragging')
            }
        }
    }
</script>

<template>
    <div 
        class="task-card-section"
        draggable="true"
        @dragstart="onDragStart"
        @dragend="onDragEnd"
        :style="{ '--base-color': baseColor }"
    >
        <div class="card-actions">
            <button 
                class="icon-btn edit-btn"
                title="Edit Task"
                @click="$emit('edit', task)"
            >
                <i class="pi pi-pencil"></i>
            </button>

            <button
                class="icon-btn delete-btn"
                title="Delete Task"
                @click="$emit('delete', task.id)"
            >
                <i class="pi pi-trash"></i>
            </button>
        </div>

        <h3 class="task-title">{{ task.task_name }}</h3>
        <p class="task-description">
            {{ task.description }}
        </p>

        <p class="due-date-text">
            Due Date: <b>{{ formattedDueDate }}</b>
        </p>
    </div>
</template>

<style scoped>
    .task-card-section {
        position: relative;
        background-color: color-mix(in srgb, var(--base-color) 30%, white);
        padding: 12px;
        border-radius: 8px;
        text-align: left;
        margin-bottom: 10px;
        isolation: isolate;
        background-clip: padding-box;
    }

    .task-card.dragging {
        opacity: 0.5;
        transform: rotate(2deg);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }

    .card-actions {
        position: absolute;
        top: -16px;
        right: 8px;
        display: flex;
        gap: 5px;
        justify-content: flex-end;
    }

    .icon-btn {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #fff;
        font-size: 14px;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }

    .icon-btn:hover {
        opacity: 0.8;
        transform: scale(1.05);
    } 

    .edit-btn {
        /* background-color: #3b82f6; */
        background-color: color-mix(in srgb, var(--base-color) 85%, black);
    }

    .delete-btn {
        background-color: #ef4444;
    }

    .task-title {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 6px;
    }

    .task-description {
        font-size: 14px;
        margin-bottom: 8px;
    }

    .due-date-text {
        font-size: 13px;
        text-align: right;
        opacity: 0.85;
    }
</style>