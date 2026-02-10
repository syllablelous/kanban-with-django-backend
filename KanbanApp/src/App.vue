<script>
  import StatusListCard from './components/StatusListCard.vue';
  import AddTaskModal from './components/AddTaskModal.vue';
  import EditTaskModal from './components/EditTaskModal.vue';
  import ConfirmDeleteModal from './components/ConfirmDeleteModal.vue';

  import {
    getTasks,
    createTask,
    updateTask,
    updateTaskStatus,
    deleteTask,
  } from './services/taskService'

  export default {
    name: "TaskManagementApp",
    components: {
      StatusListCard,
      AddTaskModal,
      EditTaskModal,
      ConfirmDeleteModal,
    },
    data() {
      return {
        tasks: [],
        statuses: ['PENDING', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED'],
        showAddModal: false,
        showEditModal: false,
        selectedTask: null,
        showDeleteModal: false,
        taskIdToDelete: null,
      }
    },
    
    async mounted() {
      await this.fetchTasks()
    },

    methods: {
      // Fetch all the tasks from the DRF backend
      async fetchTasks() {
        try {
          this.tasks = await getTasks()
        } catch (error) {
          console.error('Failed to fetch tasks:', error)
        }
      },

      // Open / close modals
      openAddModal() {
        this.showAddModal = true
      },

      closeAddModal() {
        this.showAddModal = false
      },

      openEditModal(task) {
        this.selectedTask = { ...task }
        this.showEditModal = true
      },

      closeEditModal() {
        this.selectedTask = null
        this.showEditModal = false
      },

      openDeleteModal(taskId) {
        this.taskIdToDelete = taskId
        this.showDeleteModal = true
      },

      async confirmDeleteTask() {
        try {
          await deleteTask(this.taskIdToDelete)
          this.tasks = this.tasks.filter(
            task => task.id !== this.taskIdToDelete
          )
        } catch (error) {
          console.error('Failed to delete task:', error)
        } finally {
          this.showDeleteModal = false
          this.taskIdToDelete = null
        }
      },
      cancelDeleteTask() {
        this.showDeleteModal = false
        this.taskIdToDelete = null
      },

      // Create task (POST)
      async handleCreateTask(taskData) {
        try {
          const createdTask = await createTask(taskData)
          this.tasks.push(createdTask)
          this.closeAddModal()
        } catch (error) {
          console.error('Failed to create task:', error)
        }
      },

      // Update task (PUT)
      async handleUpdateTask(updatedTask) {
        try {
          const savedTask = await updateTask(updatedTask.id, updatedTask)
          const index = this.tasks.findIndex(t => t.id === savedTask.id)

          if (index !== -1) {
            this.tasks.splice(index, 1, savedTask)
          }

          this.closeEditModal()
        } catch (error) {
          console.error('Failed to update task:', error)
        }
      },

      // Delete task (DELETE)
      // async handleDeleteTask(taskId) {
      //   try {
      //     await deleteTask(taskId)
      //     this.tasks = this.tasks.filter(task => task.id !== taskId)
      //   } catch (error) {
      //     console.error('Failed to delete task:', error)
      //   }
      // },

      async handleTaskDrop({ taskId, newStatus }) {
        const task = this.tasks.find(t => t.id === taskId)
        if (!task || task.status === newStatus) return

        task.status = newStatus

        try {
          await updateTaskStatus(taskId, newStatus)
        } catch (error) {
          console.error('Failed to update task status:', error)
        }
      }
    },
  };
</script>

<template>
  <!-- ^ Top Header Section -->
  <div class="top-section">
    <div class="title">
      <h1>My Tasks</h1>
      <p>Drag and Drop the tasks to update its status</p>
    </div>

    <button id="add-task-btn" @click="openAddModal">
      + Add Task
    </button>
  </div>

  <!-- ^ Task Columns -->
  <section class="task-list-section">
    <StatusListCard
      v-for="status in statuses"
      :key="status"
      :status="status"
      :tasks="tasks"
      @task-dropped="handleTaskDrop"
      @edit-task="openEditModal"
      @delete-task="openDeleteModal"
    />
  </section>

  <!-- ^ Add Task Modal -->
  <AddTaskModal
    v-if="showAddModal"
    @submit="handleCreateTask"
    @close="closeAddModal"
  />

  <!-- ^ Edit Task Modal -->
  <EditTaskModal
    v-if="showEditModal"
    :task="selectedTask"
    @submit="handleUpdateTask"
    @close="closeEditModal"
  />

  <ConfirmDeleteModal
    v-if="showDeleteModal"
    @confirm="confirmDeleteTask"
    @cancel="cancelDeleteTask"
  />
</template>

<style>

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 30px;
  }

  .p-component {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  }

  .top-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0px 20px 0px 20px;
    padding: 10px;
  }

  .title {
    display: flex;
    flex-direction: column;
    text-align: left;
  }

  .title h1 {
    font-weight: bold;
  }

  #add-task-btn {
    background-color: #03B57B;
    border: none;
    border-radius: 8px;
    color: white;
    padding: 15px 25px;
    /* text-align: center;
    display: inline-block; */
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color transform 1.2s;
  }

  #add-task-btn:hover {
    background-color: #039a67;
    transform: scale(0.98);
  }

  .task-list-section {
    display: flex;
    margin: 0px 25px 0px 25px;
    flex-wrap: wrap;
    gap: 10px;
  }
</style>
  