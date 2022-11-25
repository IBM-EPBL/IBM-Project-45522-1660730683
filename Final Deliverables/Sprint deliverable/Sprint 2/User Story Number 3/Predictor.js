const btn = document.getElementById("calculate");
        btn.addEventListener("click", function () 
        {
            let age = parseInt(document.querySelector("#age").value) || 0;
            let bloodurea = parseInt(document.querySelector("#bloodurea").value) || 0;
            let bloodglucoserandom = parseInt(document.querySelector("#bloodglucoserandom").value) || 0;

            if (age == 0 || bloodurea == 0 || bloodglucoserandom == 0) 
            {
                alert("Please fill out the input fields!");
                return;
            }

            if(age > 120 || age < 1){
                alert("Enter your age within limit ");
                return;
            }

            if(bloodurea > 999 || bloodurea < 0)
            {
                alert("Enter your blood urea within limit");
                return;
            }
            if(bloodglucoserandom > 999 || bloodglucoserandom < 0)
            {
                alert("Enter your blood glucose random within limit");
                return;
            }
        }
        );