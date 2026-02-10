<!-- TODO: Adjust the date here so that it will accommodate the datetimefield specified in the backend -->
<script>
    import Dialog from 'primevue/dialog'
    import Button from 'primevue/button'
    import InputText from 'primevue/inputtext'
    import Textarea from 'primevue/textarea'
    import Calendar from 'primevue/calendar'
    import Dropdown from 'primevue/dropdown'

    export default {
        name: 'EditTaskModal',
        props: {
            task: {
                type: Object,
                required: true,
            },
        },
        emits: ['submit', 'close'],
        data() {
            return {
                form: {
                    id: null,
                    task_name: '',
                    description: '',
                    due_date: null,
                    status: '',
                },
                statusOptions: [
                    { label: 'Pending', value: 'PENDING' },
                    { label: 'In Progress', value: 'IN_PROGRESS' },
                    { label: 'Completed', value: 'COMPLETED' },
                    { label: 'Cancelled', value: 'CANCELLED' },
                ],
            }
        },
        mounted() {
            this.form.id = this.task.id
            this.form.task_name = this.task.task_name
            this.form.description = this.task.description
            this.form.status = this.task.status
            this.form.due_date = this.parseDateTime(this.task.due_date)
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

                this.$emit('submit', {
                    id: this.form.id,
                    task_name: this.form.task_name,
                    description: this.form.description,
                    due_date: this.formatDateTime(this.form.due_date),
                    status: this.form.status,
                })
            },

            closeModal() {
                this.$emit('close')
            },

            parseDateTime(dateTimeString) {
                return dateTimeString ? new Date(dateTimeString) : null
            },

            formatDateTime(date) {
                return date.toISOString()
            },
        },   
    }
</script>

<template>
    <Dialog
        header="Edit Task"
        :visible="true"
        modal
        :closable="false"
        style="width: 400px"
    >
        <div class="form-group">
            <label>Title</label>
            <InputText v-model="form.task_name" />
        </div>
        
        <div class="form-group">
            <label>Description</label>
            <Textarea v-model="form.description" rows="3" />
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
                optionLabel="label"
                optionValue="value"
            />
        </div>

        <template #footer>
            <Button
                label="Cancel"
                severity="secondary"
                @click="closeModal"
            />

            <Button
                label="Save Changes"
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