const getAccount = async (username) => {
    fetch(`http://localhost:8080/accounts/${username}`, {mode: 'cors'})
    .then(res => res.json()
        .then(data => {
            return {
                name: data.name,
                username: data.username,
                email: data.email,
            }
        })
    ).then(res => updateOutput(res))
    .catch(updateOutput(null));
}

const createAccount = async (name, username, email) => {
    const data = {
        name: name,
        username: username,
        email: email,
    };

    fetch(`http://localhost:8080/accounts/`, {
        method: "POST",
        mode: 'cors',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
}

const deleteAccount = async (username) => {
    fetch(`http://localhost:8080/accounts/${username}`, {
        method: "DELETE",
        mode: 'cors',
    });
}

// Update Output window
const updateOutput = (data) => {
    if (data) {
        document.querySelector('#output-root').innerHTML = `
            <h3>name: ${data.name}</h3>
            <h3>username: ${data.username}</h3>
            <h3>email: ${data.email}</h3>
        `;
    } else {
        document.querySelector('#output-root').innerHTML = `
            <h3>Account does not exist</h3>
        `;
    }
}