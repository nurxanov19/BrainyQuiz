// Dummy Quiz Data
const quizzes = [
    {
        id: 1,
        title: "General Knowledge Trivia",
        description: "Test your general knowledge!",
        category: "Science",
        difficulty: "Easy",
        questions: 5,
        details: [
            { question: "What is the capital of France?", options: ["Paris", "London", "Berlin", "Madrid"], correct: 0 },
            { question: "Which planet is the Red Planet?", options: ["Jupiter", "Mars", "Venus", "Mercury"], correct: 1 }
        ]
    },
    {
        id: 2,
        title: "Math Challenge",
        description: "Solve these math problems!",
        category: "Math",
        difficulty: "Medium",
        questions: 3,
        details: [
            { question: "What is 2 + 2?", options: ["3", "4", "5", "6"], correct: 1 }
        ]
    }
];

// Quizzes Page
if (document.getElementById('quizContainer')) {
    displayQuizzes(quizzes);
    document.getElementById('quizSearch').addEventListener('input', filterQuizzes);
    document.getElementById('categoryFilter').addEventListener('change', filterQuizzes);
    document.getElementById('difficultyFilter').addEventListener('change', filterQuizzes);

    function displayQuizzes(quizArray) {
        const container = document.getElementById('quizContainer');
        container.innerHTML = quizArray.map(quiz => `
            <div class="col-md-4 mb-4">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">${quiz.title}</h5>
                        <p class="card-text">${quiz.description}</p>
                        <p><strong>Category:</strong> ${quiz.category}</p>
                        <p><strong>Difficulty:</strong> ${quiz.difficulty}</p>
                        <p><strong>Questions:</strong> ${quiz.questions}</p>
                        <a href="quiz.html?id=${quiz.id}" class="btn btn-primary">Start</a>
                    </div>
                </div>
            </div>
        `).join('');
    }

    function filterQuizzes() {
        const search = document.getElementById('quizSearch').value.toLowerCase();
        const category = document.getElementById('categoryFilter').value;
        const difficulty = document.getElementById('difficultyFilter').value;
        let filtered = quizzes.filter(quiz =>
            quiz.title.toLowerCase().includes(search) &&
            (!category || quiz.category === category) &&
            (!difficulty || quiz.difficulty === difficulty)
        );
        displayQuizzes(filtered);
    }
}

// Quiz Taking Page
if (document.getElementById('questionContainer')) {
    const quizId = new URLSearchParams(window.location.search).get('id');
    const quiz = quizzes.find(q => q.id == quizId);
    if (quiz) {
        let currentQuestion = 0;
        let answers = new Array(quiz.details.length).fill(null);
        let timeLeft = 600;

        document.getElementById('quizTitle').textContent = quiz.title;
        displayQuestion();

        const timer = setInterval(() => {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            document.getElementById('timer').textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
            if (timeLeft <= 0) submitQuiz();
        }, 1000);

        function displayQuestion() {
            const q = quiz.details[currentQuestion];
            document.getElementById('questionContainer').innerHTML = `
                <h4>Question ${currentQuestion + 1} of ${quiz.details.length}</h4>
                <p>${q.question}</p>
                <div class="list-group">
                    ${q.options.map((opt, i) => `
                        <button class="list-group-item list-group-item-action option ${answers[currentQuestion] === i ? 'selected' : ''}" data-index="${i}">
                            ${opt}
                        </button>
                    `).join('')}
                </div>
            `;
            document.getElementById('prevBtn').disabled = currentQuestion === 0;
            document.getElementById('nextBtn').textContent = currentQuestion === quiz.details.length - 1 ? 'Submit' : 'Next';
            document.querySelectorAll('.option').forEach(btn => {
                btn.addEventListener('click', () => {
                    answers[currentQuestion] = parseInt(btn.dataset.index);
                    displayQuestion();
                });
            });
        }

        document.getElementById('prevBtn').addEventListener('click', () => {
            currentQuestion--;
            displayQuestion();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            if (currentQuestion < quiz.details.length - 1) {
                currentQuestion++;
                displayQuestion();
            } else {
                submitQuiz();
            }
        });

        function submitQuiz() {
            clearInterval(timer);
            let score = quiz.details.reduce((acc, q, i) => acc + (answers[i] === q.correct ? 1 : 0), 0);
            document.querySelector('.quiz-section .card').classList.add('d-none');
            const result = document.getElementById('resultContainer');
            result.classList.remove('d-none');
            document.getElementById('scoreText').textContent = `You scored ${score} out of ${quiz.details.length}!`;
            for (let i = 0; i < 100; i++) {
                const confetti = document.createElement('div');
                confetti.style.cssText = `
                    position: absolute; top: 0; left: ${Math.random() * 100}%;
                    width: 10px; height: 10px; background: hsl(${Math.random() * 360}, 100%, 50%);
                    animation: fall ${Math.random() * 2 + 1}s linear;
                `;
                document.getElementById('confetti').appendChild(confetti);
            }
        }
    }
}

// Add Quiz Page
if (document.getElementById('addQuizForm')) {
    let questionCount = 0;
    document.getElementById('addQuestionBtn').addEventListener('click', () => {
        questionCount++;
        const container = document.getElementById('questionsContainer');
        container.innerHTML += `
            <div class="question-block">
                <h5>Question ${questionCount}</h5>
                <div class="mb-3">
                    <label class="form-label">Question Text</label>
                    <input type="text" class="form-control" required>
                </div>
                <div class="row">
                    ${[1, 2, 3, 4].map(i => `
                        <div class="col-md-6 mb-2">
                            <label class="form-label">Option ${i}</label>
                            <input type="text" class="form-control" required>
                        </div>
                    `).join('')}
                </div>
                <div class="mb-3">
                    <label class="form-label">Correct Answer</label>
                    <select class="form-select" required>
                        <option value="">Select Correct Answer</option>
                        ${[0, 1, 2, 3].map(i => `<option value="${i}">Option ${i + 1}</option>`).join('')}
                    </select>
                </div>
            </div>
        `;
        container.lastElementChild.scrollIntoView({ behavior: 'smooth' });
    });

    document.getElementById('addQuizForm').addEventListener('submit', e => {
        e.preventDefault();
        if (questionCount === 0) alert('Add at least one question.');
        else alert('Quiz created successfully! (Frontend only)');
    });
}

// Login/Register Page
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', e => {
        e.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        if (username && password) alert('Logged in! (Frontend only)');
        else alert('Fill in all fields.');
    });

    document.getElementById('registerForm').addEventListener('submit', e => {
        e.preventDefault();
        const username = document.getElementById('registerUsername').value;
        const email = document.getElementById('registerEmail').value;
        const password = document.getElementById('registerPassword').value;
        const confirm = document.getElementById('confirmPassword').value;
        if (username && email && password && confirm) {
            if (password === confirm) alert('Registered! (Frontend only)');
            else alert('Passwords do not match.');
        } else alert('Fill in all fields.');
    });
}

// Profile Page
if (document.getElementById('quizHistory')) {
    const history = [
        { title: "General Knowledge Trivia", category: "Science", score: "4/5", date: "2025-04-10" },
        { title: "Math Challenge", category: "Math", score: "2/3", date: "2025-04-12" }
    ];
    document.getElementById('quizHistory').innerHTML = history.map(item => `
        <tr>
            <td>${item.title}</td>
            <td>${item.category}</td>
            <td>${item.score}</td>
            <td>${item.date}</td>
        </tr>
    `).join('');
}