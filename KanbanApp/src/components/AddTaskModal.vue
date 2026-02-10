
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
                form: {
                    task_name: '',
                    description: '',
                    due_date: null,
                    status: 'PENDING',
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
        methods: {
            submitForm() {
                if (!this.form.task_name || !this.form.due_date) {
                    alert('Task name and due date are required.')
                    return
                }

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
            <InputText v-model="form.task_name" placeholder="Task Name" />
        </div>
        
        <div class="form-group">
            <label>Description</label>
            <Textarea v-model="form.description" rows="3" placeholder="Task Description" />
        </div>

        <div class="form-group">
            <label>Due Date & Time</label>
            <Calendar
                v-model="form.due_date"
                showIcon
                showTime
                hourFormat="24"
                dateFormat="yy-mm-dd"
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
</style>