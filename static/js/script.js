window.onload = function () {
    document.getElementById('question19').style.display = 'block'
    UpdateData()
}

function UpdateData() {
    let buttons = document.querySelectorAll('.btn')
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            let questNum = parseInt(button.getAttribute('data-question'))
            let questValue = button.innerText

            let data = {
                questNum: questNum,
                questValue: questValue
            }

            fetch('/checkAnswer', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(result => {
                    if (result.result){
                        let questionButtons = document.querySelectorAll(`.btn[data-question="${questNum}"]`);
                        questionButtons.forEach(qButton => {
                            qButton.disabled = true;
                        });

                        if (result.correctAnswer){
                            button.style.backgroundColor = 'lightgreen'
                            button.style.color = 'black'
                        }
                        else {
                            button.style.backgroundColor = 'red'
                            button.style.color = 'black'
                        }


                         setTimeout(function () {
                             if (parseInt(questNum) < 20){
                                 document.getElementById('question' + questNum).style.display = 'none'
                                 let nextQuest = parseInt(questNum)+1
                                 document.getElementById('question' + nextQuest).style.display = 'block'
                             }
                             else {
                                 window.location.href = '/result'
                             }
                         }, 3000)


                    }
                    else {
                        alert(result.message)
                    }
                })
        })
    })
}
