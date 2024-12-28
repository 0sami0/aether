    fetch("https://samihil.pythonanywhere.com/new_bid",{
        method: 'POST',
         headers: {
            'Content-Type': 'application/json',
          },
        body: JSON.stringify({
                "job_title": "Test Data Entry Job",
                "response": "This is a test automated response for the data entry job. I hope you like it",
                "platform": "Test"
            })
    }).then(response => response.json()).then(data => console.log(data)).catch((error) => {
       console.error("Error:", error);
     });
