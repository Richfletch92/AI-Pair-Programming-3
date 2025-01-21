document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.task-completed-checkbox');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.getAttribute('data-task-id');
            const completed = this.checked;

            fetch(`/tasks/${taskId}/update/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ completed: completed })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const taskRow = this.closest('tr');
                    if (completed) {
                        document.querySelector('#done-tasks tbody').appendChild(taskRow);
                    } else {
                        document.querySelector('#todo-tasks tbody').appendChild(taskRow);
                    }
                } else {
                    console.error('Failed to update task');
                }
            });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}