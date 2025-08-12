document.querySelectorAll('.task').forEach(task => {
    task.addEventListener('dragstart', () => {
        task.classList.add('dragging');
    });
    task.addEventListener('dragend', () => {
        task.classList.remove('dragging');
    });
});

document.querySelectorAll('.column').forEach(column => {
    column.addEventListener('dragover', e => {
        e.preventDefault();
        const task = document.querySelector('.dragging');
        column.appendChild(task);
    });
});