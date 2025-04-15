document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu');
    const navMenu = document.querySelector('nav ul');

    mobileMenuBtn.addEventListener('click', function() {
        navMenu.classList.toggle('show');
    });

    // Test Package Filtering
    const filterButtons = document.querySelectorAll('.filter-btn');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');

            // Here you would filter the test packages based on the category
            // For now, we'll just log the category
            const category = this.textContent.trim();
            console.log(`Filtering by: ${category}`);

            // In a real implementation, you would:
            // 1. Hide all test cards
            // 2. Show only those that match the selected category
            // 3. Or make an AJAX request to get filtered results
        });
    });

    // Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Floating Brain Animation - Create additional floating brains dynamically
    function createFloatingBrains() {
        const colors = ['#6c63ff', '#ff6584', '#4d44db', '#2d2d3a'];
        const container = document.body;

        for (let i = 0; i < 5; i++) {
            const brain = document.createElement('div');
            brain.className = 'floating-brain dynamic';

            // Random properties
            const size = Math.random() * 60 + 40; // 40-100px
            const posX = Math.random() * 100; // 0-100%
            const posY = Math.random() * 100; // 0-100%
            const delay = Math.random() * 5; // 0-5s
            const duration = Math.random() * 4 + 4; // 4-8s
            const color = colors[Math.floor(Math.random() * colors.length)];

            brain.style.width = `${size}px`;
            brain.style.height = `${size}px`;
            brain.style.left = `${posX}%`;
            brain.style.top = `${posY}%`;
            brain.style.animationDelay = `${delay}s`;
            brain.style.animationDuration = `${duration}s`;
            brain.style.backgroundColor = color;
            brain.style.borderRadius = '50%';
            brain.style.opacity = '0.1';

            container.appendChild(brain);
        }
    }

    createFloatingBrains();

    // Newsletter Form Submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();

            if (email) {
                // Here you would typically send the email to your server
                console.log(`Subscribing email: ${email}`);
                alert('Thank you for subscribing to our newsletter!');
                emailInput.value = '';
            }
        });
    }

    // Scroll Animation - Animate elements when they come into view
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.feature-card, .test-card');

        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    // Set initial state for animated elements
    document.querySelectorAll('.feature-card, .test-card').forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    // Run once on load
    animateOnScroll();

    // Run on scroll
    window.addEventListener('scroll', animateOnScroll);
});