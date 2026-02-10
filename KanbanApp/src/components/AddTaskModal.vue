
<script>
    import Dialog from 'primevue/dialog'
    import Button from 'primevue/button'
    import InputText from 'primevue/inputtext'
    import Textarea from 'primevue/textarea'
    import Calendar from 'primevue/calendar'
    import Dropdown from 'primevue/dropdown'

    export default {
        name: 'AddTaskModal',
        emits: ['submit', 'close'],
        data() {
            return {
                today: new Date(),
                form: {
                    task_name: '',
                    description: '',
                    due_date: null,
                    status: 'PENDING',
                },
                limits: {
                    task_name: 100,
                    description: 500,
                },
                statusOptions: [
                    { label: 'Pending', value: 'PENDING' },
                    { label: 'In Progress', value: 'IN_PROGRESS' },
                    { label: 'Completed', value: 'COMPLETED' },
                    { label: 'Cancelled', value: 'CANCELLED' },
                ],
            }
        },
        components: {
            Dialog,
            Button,
            InputText,
            Textarea,
            Calendar,
            Dropdown,
        },
        computed: {
            isFormValid() {
                return (
                    this.form.task_name.trim().length > 0 &&
                    this.form.description.trim().length > 0 &&
                    this.form.due_date !== null
                )
            },
        },
        methods: {
            submitForm() {
                if (!this.isFormValid) return

                const payload = {
                    task_name: this.form.task_name,
                    description: this.form.description,
                    due_date: this.formatDateTime(this.form.due_date),
                    status: this.form.status,
                }

                this.$emit('submit', payload)
            },

            closeModal() {
                this.$emit('close')
            },

            formatDateTime(date) {
                return date.toISOString();
            },
        },   
    }
</script>

<template>
    <Dialog
        header="Add New Task"
        :visible="true"
        modal
        :closable="false"
        style="width: 400px"
    >
        <div class="form-group">
            <label>Title</label>
            <InputText 
                v-model="form.task_name" 
                :maxlength="limits.task_name"
                placeholder="Task Name" 
            />
            <small>{{ form.task_name.length }} / {{ limits.task_name }}</small>
        </div>
        
        <div class="form-group">
            <label>Description</label>
            <Textarea 
                v-model="form.description" 
                :maxlength="limits.description"
                rows="3" 
                placeholder="Task Description" 
            />
            <small>{{ form.description.length }} / {{ limits.description }}</small>
        </div>

        <div class="form-group">
            <label>Due Date & Time</label>
            <Calendar
                v-model="form.due_date"
                showIcon
                showTime
                hourFormat="24"
                dateFormat="yy-mm-dd"
                :minDate="today"
            />
        </div>

        <div class="form-group">
            <label>Status</label>
            <Dropdown
                v-model="form.status"
                :options="statusOptions"
                optionValue="value"
                optionLabel="label"
                placeholder="Select status"
            />
        </div>

        <template #footer>
            <Button
                label="Cancel"
                severity="secondary"
                @click="closeModal"
            />

            <Button
                label="Add Task"
                icon="pi pi-check"
                :disabled="!isFormValid"
                @click="submitForm"
            />
        </template>
    </Dialog>
</template>

<style scoped>

    .form-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 15px;
    }

    .form-group label {
        font-weight: bold;
        margin-bottom: 5px;
    }

    small {
        color: #6b7280;
        font-size: 0.75rem;
    }
</style>