<script>
    import Dialog from 'primevue/dialog'
    import Button from 'primevue/button'

    export default {
        name: 'ConfirmDeleteModal',
        emits: ['confirm', 'cancel'],
        components: {
            Dialog,
            Button,
        },
    }
</script>

<template>
    <Dialog
        header="Confirm Delete"
        :visible="true"
        modal
        :closable="false"
        style="width: 350px"
    >
        <p>
            Are you sure you want to delete this task?
            <br />
            <b>This action cannot be undone.</b>
        </p>

        <template #footer>
            <Button
                label="Cancel"
                severity="secondary"
                @click="$emit('cancel')"
            />
            <Button
                label="Delete"
                severity="danger"
                @click="$emit('confirm')"
            />
        </template>
    </Dialog>
</template>

<style scoped>
    p {
        margin: 0;
        line-height: 1.5;
    }
</style>