async function addUser(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    try {
        // Send POST request
        const response = await fetch('/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email })
        });

        if (response.ok) {
            document.getElementById('name').value = '';
            document.getElementById('email').value = '';

            const users = await response.json();
            updateUserList(users);
        } else {
            console.error('Could not add user: ', response.statusText);
        }
    } catch (error) {
        console.error('Error: ', error);
    }
}

function updateUserList(users) {
    // Update the user list on the page
    const userList = document.getElementById('user-list');
    userList.innerHTML = '';

    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = `${user[0]} (${user[1]})`;
        userList.appendChild(li);
    });
}