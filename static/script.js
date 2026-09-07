function toggleMenu() {

    const menu =
        document.querySelector(".nav-links");

    menu.classList.toggle("active");
}


document
    .getElementById("registrationForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();

        const message =
            document.getElementById("message");

        const data = {

            name:
                document.getElementById("name").value,

            email:
                document.getElementById("email").value,

            phone:
                document.getElementById("phone").value,

            college:
                document.getElementById("college").value,

            event:
                document.getElementById("event").value

        };


        message.innerHTML = "Submitting...";


        try {

            const response =
                await fetch("/register", {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(data)

                });


            const result =
                await response.json();


            if (result.success) {

                message.innerHTML =
                    "✅ " +
                    result.message +
                    "<br>Registration ID: #" +
                    result.registration_id;

                message.style.color = "green";

                document
                    .getElementById("registrationForm")
                    .reset();

            } else {

                message.innerHTML =
                    "❌ " + result.message;

                message.style.color = "red";

            }

        }

        catch (error) {

            console.error(error);

            message.innerHTML =
                "❌ Server connection failed.";

            message.style.color = "red";

        }

    });