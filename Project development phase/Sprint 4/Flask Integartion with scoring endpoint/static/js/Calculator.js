const btn = document.getElementById("calculate");
        btn.addEventListener("click", function () 
        {
            let height = parseInt(document.querySelector("#height").value) || 0;
            let weight = parseInt(document.querySelector("#weight").value) || 0;
            if (height == 0 || weight == 0 ) 
            {
                alert("Please fill out the input fields!");
                return;
            }
            if(height > 251 || height < 29){
                alert("Enter your height within limit (30-250)");
                return;
            }
            if(weight > 251 || weight < 1)
            {
                alert("Enter your weight within limit (1-250)");
                return;
            }
            height = height / 100;
            let BMI = weight / (height * height);
            BMI = BMI.toFixed(2);
            document.querySelector("#result").innerHTML = BMI;
            let status = "";
            if (BMI < 18.5) 
            {
                status = "Underweight!! try to increase your weight";
            }
            if (BMI >= 18.5 && BMI < 25) 
            {
                status = "Healthy";
            }
            if (BMI >= 25 && BMI < 30) 
            {
                status = "Overweight!! try to reduce your weight to be healthy";
            }
            if (BMI >= 30) 
            {
                status = "Obese!! fat content is too much in your body, must reduce your weight";
            }
            document.querySelector(".comment").innerHTML = `Comment: you are <span id="comment">${status}</span>`;
        });