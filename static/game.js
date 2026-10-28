let level = 1;
let randomNumber;
let score = 0;

function startGame() {
    document.getElementById("level").innerText = `LEVEL ${level}`;
    document.getElementById("score").innerText = `SCORE: ${String(score).padStart(8, '0')}`;
    generateRandomNumber();
}

function generateRandomNumber() {
    let max;
    if (level <= 4) max = 8;
    else if (level <= 8) max = 16;
    else if (level <= 12) max = 32;
    else if (level <= 16) max = 64;
    else if (level <= 20) max = 128;
    else if (level <= 24) max = 256;
    else max = 511;

    randomNumber = Math.floor(Math.random() * (max + 1));
    document.getElementById("random-number").innerText = randomNumber;
}

function toggleCell(index) {
    let row1 = document.getElementById("row1").children;
    row1[index].innerText = row1[index].innerText === "0" ? "1" : "0";
}

function resetRow() {
    let row1 = document.getElementById("row1").children;
    for (let i = 0; i < row1.length; i++) {
        row1[i].innerText = "0";
    }
}

function checkAnswer() {
    let row1 = document.getElementById("row1").children;
    let userNumber = 0;
    for (let i = 0; i < row1.length; i++) {
        if (row1[i].innerText === "1") {
            userNumber += Math.pow(2, 8 - i);
        }
    }

    if (userNumber === randomNumber) {
        level++;
        score += 5;
        resetRow();

        // Add fade-out and fade-in during level changes
        const levelContainers = document.querySelectorAll('.fade-container');
        levelContainers.forEach(levelContainer => {
            levelContainer.classList.add("fade");
            setTimeout(() => {
                levelContainer.classList.add("in");
                // Change level here
                startGame();
                // Remove classes after transition
                setTimeout(() => {
                    levelContainer.classList.remove("fade", "in");
                }, 500);
            }, 500);
        });

    } else {

        const levelContainers = document.querySelectorAll('.fade-container');
        levelContainers.forEach(levelContainer => {
            levelContainer.classList.add("fade");
            setTimeout(() => {
                levelContainer.classList.add("in");
                // Show Game Over screen
                fetch('/save-score', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ score: score })
                });
                document.body.innerHTML = "<div class=\"middle\"> <p class=\"white-text center\">GAME OVER</p> <a class=\"lavender-text center\" href=\"/start\">RESTART</a> <a class=\"lavender-text center\" href=\"/\">EXIT</a> </div>";
                // Remove classes after transition
                setTimeout(() => {
                    levelContainer.classList.remove("fade", "in");
                }, 500);
            }, 500);
        });
    }
}

startGame();
