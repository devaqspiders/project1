const BASE_URL = "http://127.0.0.1:1431";

const output = document.getElementById("output");

function showData(data) {
    output.textContent = JSON.stringify(data, null, 4);
}

async function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {

        const response = await fetch(`${BASE_URL}/api/token/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "user_email" : username,
                "password" : password
            })
        });

        const data = await response.json();

        if (response.ok) {

            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);

            showData({
                message: "Login successful"
            });

        } else {
            showData(data);
        }

    } catch (error) {
        console.error(error);
    }
}

async function refreshToken() {

    const refresh = localStorage.getItem("refresh");

    try {

        const response = await fetch(
            `${BASE_URL}/api/token/refresh/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    refresh
                })
            }
        );

        const data = await response.json();

        if (response.ok) {

            localStorage.setItem("access", data.access);

            showData({
                message: "Access token refreshed"
            });

        } else {
            showData(data);
        }

    } catch (error) {
        console.error(error);
    }
}

async function authorizedFetch(url) {

    let access = localStorage.getItem("access");

    let response = await fetch(url, {
        headers: {
            Authorization: `Bearer ${access}`
        }
    });

    if (response.status === 401) {

        await refreshToken();

        access = localStorage.getItem("access");

        response = await fetch(url, {
            headers: {
                Authorization: `Bearer ${access}`
            }
        });
    }

    return response;
}

async function getUsers() {

    try {

        const response = await authorizedFetch(
            `${BASE_URL}/api/v1/user/`
        );

        const data = await response.json();

        showData(data);

    } catch (error) {
        console.error(error);
    }
}

async function getTasks() {

    try {

        const response = await authorizedFetch(
            `${BASE_URL}/api/v1/task/`
        );

        const data = await response.json();

        showData(data);

    } catch (error) {
        console.error(error);
    }
}

document
    .getElementById("loginBtn")
    .addEventListener("click", login);

document
    .getElementById("refreshBtn")
    .addEventListener("click", refreshToken);

document
    .getElementById("getUsersBtn")
    .addEventListener("click", getUsers);

document
    .getElementById("getTasksBtn")
    .addEventListener("click", getTasks);