// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger);

// Initialize Lenis (Smooth Scroll)
const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
});

// Get scroll value for GSAP
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);


// --- PROJECT DATA ---
const projectsData = {
    "whatsapp-bot": {
        title: "TurnoFlow",
        subtitle: "WhatsApp Booking SaaS",
        description: "<p>Este proyecto es un sistema integral de reservas automatizado vía WhatsApp, diseñado como un <strong>SaaS Multi-Tenant (Multi-Barbería)</strong>. Permite a múltiples barberías usar un mismo servidor para que sus clientes autogestionen turnos 24/7 de forma 100% aislada.</p><ul><li><strong>Arquitectura Multi-Barbería:</strong> Un solo servidor para múltiples clientes.</li><li><strong>Bot Inteligente:</strong> API Oficial de Meta Cloud.</li><li><strong>Panel PWA:</strong> Dashboard 'Glassmorphism' instalable.</li><li><strong>Prevención de Doble Reserva:</strong> Control de concurrencia estricto.</li></ul>",
        tags: ["Python", "FastAPI", "Supabase", "Meta API", "Vercel"],
        demo: null,
        github: "https://github.com/BrocatoSantino/whatsapp-bot"
    },
    "StudioArq-landing": {
        title: "StudioArq",
        subtitle: "Arquitectura y Diseño",
        description: "<p>Landing page de demostración para un estudio de arquitectura y diseño de interiores. Diseño hiper-minimalista, con una estética puramente editorial orientada a resaltar la belleza de los materiales, la luz y los proyectos a gran escala.</p><ul><li><strong>Hero Inmersivo:</strong> Background image a pantalla completa con tipografía gigante.</li><li><strong>Visión:</strong> Layout asimétrico a dos columnas.</li><li><strong>Proyectos:</strong> Sistema de Film Strip con scroll horizontal.</li><li><strong>Formulario Brutalista:</strong> Sin fondo ni caja, solo bordes finos.</li></ul>",
        tags: ["HTML5", "TailwindCSS", "JavaScript", "Minimalismo"],
        demo: "https://brocatosantino.github.io/StudioArq-landing/",
        github: "https://github.com/BrocatoSantino/StudioArq-landing"
    },
    "nexadigital-landing-page": {
        title: "NexaDigital",
        subtitle: "Agencia de Marketing",
        description: "<p>Landing page de demostración para una agencia de marketing digital. Diseño limpio, corporativo y moderno con micro-animaciones y optimización para conversión.</p><ul><li><strong>Hero Dinámico:</strong> Título fuerte con doble CTA.</li><li><strong>Servicios:</strong> Tarjetas interactivas con hover elevation.</li><li><strong>Testimonios:</strong> Prueba social con rating de estrellas.</li><li><strong>Diseño Optimizado:</strong> Sin dependencias, JS Vanilla puro.</li></ul>",
        tags: ["Tailwind v4", "UX/UI", "JavaScript", "HTML5"],
        demo: "https://brocatosantino.github.io/nexadigital-landing-page/",
        github: "https://github.com/BrocatoSantino/nexadigital-landing-page"
    },
    "weather-api-wrapper": {
        title: "Weather API Wrapper",
        subtitle: "Servicio RESTful",
        description: "<p>Una API construida con FastAPI que obtiene y devuelve datos meteorológicos de la API de Visual Crossing. Este proyecto implementa llamadas a APIs de terceros y manejo de historial en base de datos.</p><ul><li><strong>FastAPI & Uvicorn:</strong> Backend robusto y asíncrono.</li><li><strong>SQLAlchemy & SQLite:</strong> Base de datos para guardar el historial.</li><li><strong>Variables de entorno:</strong> Configuración segura de API Keys.</li></ul>",
        tags: ["Python", "FastAPI", "SQLAlchemy", "Requests"],
        demo: null,
        github: "https://github.com/BrocatoSantino/weather-api-wrapper"
    },
    "to-do-list-API": {
        title: "To-Do List API",
        subtitle: "CRUD Backend",
        description: "<p>Una API RESTful construida con FastAPI para gestionar tareas (To-Do List). Este proyecto implementa operaciones CRUD completas (Create, Read, Update, Delete) utilizando una base de datos relacional y separación de responsabilidades mediante esquemas de validación.</p><ul><li><strong>Pydantic:</strong> Validación de datos estricta.</li><li><strong>SQLAlchemy:</strong> ORM para interactuar con la DB de forma segura.</li><li><strong>Arquitectura Limpia:</strong> Separación de modelos, rutas y controladores.</li></ul>",
        tags: ["Python", "FastAPI", "SQLite", "Pydantic"],
        demo: null,
        github: "https://github.com/BrocatoSantino/to-do-list-API"
    },
    "CortesAndCo": {
        title: "Cortes & Co.",
        subtitle: "Landing Page de Barbería",
        description: "<p>Landing page moderna y atractiva para una barbería local, enfocada en la reserva de turnos rápida y en mostrar el estilo del local. Su objetivo es convertir visitantes en clientes a través de un diseño visual fuerte y llamadas a la acción claras.</p>",
        tags: ["HTML5", "CSS3", "Responsive Design"],
        demo: "https://brocatosantino.github.io/CortesAndCo/",
        github: "https://github.com/BrocatoSantino/CortesAndCo"
    },
    "ServicioYa-landing": {
        title: "ServicioYa",
        subtitle: "Landing de Servicios Multi-rubro",
        description: "<p>Plataforma para ofrecer servicios a domicilio. Presenta un diseño de alta confianza, enfocado en mostrar beneficios, testimonios y una interfaz limpia para que los usuarios soliciten profesionales de manera sencilla.</p>",
        tags: ["HTML5", "TailwindCSS", "UI/UX"],
        demo: "https://brocatosantino.github.io/ServicioYa-landing/",
        github: "https://github.com/BrocatoSantino/ServicioYa-landing"
    },
    "aura-boutique-catalog": {
        title: "AURA Boutique",
        subtitle: "Catálogo de Moda",
        description: "<p>Un elegante catálogo online para una marca de ropa boutique. Resalta las colecciones a través de galerías de imágenes de alta resolución, combinando el minimalismo con tipografías fashion-forward y transiciones fluidas.</p>",
        tags: ["HTML5", "CSS Animations", "JavaScript"],
        demo: "https://brocatosantino.github.io/aura-boutique-catalog/",
        github: "https://github.com/BrocatoSantino/aura-boutique-catalog"
    }
};


// --- ANIMATIONS & LOGIC ---
document.addEventListener("DOMContentLoaded", () => {
    
    // 0. Footer Reveal Logic
    function setFooterReveal() {
        const footer = document.querySelector('.footer-wrapper');
        const mainContent = document.querySelector('.main-content');
        if (footer && mainContent) {
            mainContent.style.marginBottom = `${footer.offsetHeight}px`;
        }
    }
    setFooterReveal();
    window.addEventListener('resize', setFooterReveal);

    // 1. Hero Entrance Timeline
    const tl = gsap.timeline({ defaults: { ease: "power4.out", duration: 1.2 } });
    
    tl.from(".gsap-reveal", {
        y: 100,
        opacity: 0,
        stagger: 0.1,
        delay: 0.2
    });

    // --- SUBTLE STARS BACKGROUND ---
    const mainContent = document.querySelector('.main-content');
    if(mainContent) {
        for(let i=0; i<30; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.animationDelay = `${Math.random() * 5}s`;
            mainContent.appendChild(star);
        }
    }

    // 2. Parallax Images
    gsap.utils.toArray('.gsap-parallax-img').forEach(img => {
        gsap.fromTo(img, {
            yPercent: -10
        }, {
            yPercent: 10,
            ease: "none",
            scrollTrigger: {
                trigger: img.parentElement,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    });

    // 3. Fade up Sections
    gsap.utils.toArray('.gsap-fade').forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
            },
            y: 40,
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });

    // 4. Staggered Project Cards
    gsap.utils.toArray('.projects-grid').forEach(grid => {
        const cards = grid.querySelectorAll('.gsap-card');
        gsap.from(cards, {
            scrollTrigger: {
                trigger: grid,
                start: "top 80%",
            },
            y: 50,
            opacity: 0,
            duration: 1,
            stagger: 0.15,
            ease: "power3.out"
        });
    });

    // 5. Footer Reveal Animation
    gsap.from('.gsap-footer-reveal', {
        scrollTrigger: {
            trigger: '.footer-wrapper',
            start: "top bottom", 
            end: "bottom bottom",
            scrub: true
        },
        y: -50,
        opacity: 0,
        stagger: 0.1
    });

    // --- MAGNETIC BUTTONS ---
    const magnets = document.querySelectorAll('.magnetic-btn');
    magnets.forEach(btn => {
        btn.addEventListener('mousemove', function(e) {
            const rect = btn.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            const x = (e.clientX - centerX) * 0.15;
            const y = (e.clientY - centerY) * 0.15;
            
            gsap.to(btn, {
                x: x,
                y: y,
                duration: 0.5,
                ease: "power2.out"
            });
            
            const text = btn.querySelector('.magnetic-text');
            if(text) {
                gsap.to(text, {
                    x: x * 0.5,
                    y: y * 0.5,
                    duration: 0.5,
                    ease: "power2.out"
                });
            }
        });

        btn.addEventListener('mouseleave', function(e) {
            gsap.to(btn, {
                x: 0,
                y: 0,
                duration: 0.7,
                ease: "elastic.out(1, 0.3)"
            });
            const text = btn.querySelector('.magnetic-text');
            if(text) {
                gsap.to(text, {
                    x: 0,
                    y: 0,
                    duration: 0.7,
                    ease: "elastic.out(1, 0.3)"
                });
            }
        });
    });

    // --- LOGO CLICK TO TOP ---
    const logoLink = document.getElementById('logo-link');
    if(logoLink) {
        logoLink.addEventListener('click', (e) => {
            e.preventDefault();
            lenis.scrollTo(0, { duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
        });
    }

    // --- HAMBURGER MENU ---
    const menuBtn = document.getElementById('menu-toggle-btn');
    const navPanel = document.getElementById('nav-panel');

    if (menuBtn && navPanel) {
        menuBtn.addEventListener('click', () => {
            menuBtn.classList.toggle('active');
            navPanel.classList.toggle('open');
        });
    }

    // --- SMOOTH SCROLL ANCHORS ---
    document.querySelectorAll('a.nav-menu-link, .hero-actions a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            
            // Close mobile menu if open
            if (menuBtn.classList.contains('active')) {
                menuBtn.classList.remove('active');
                navPanel.classList.remove('open');
            }

            if (targetId === '#contacto') {
                lenis.scrollTo(document.body.scrollHeight, { duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
            } else {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    lenis.scrollTo(targetElement, { offset: -30, duration: 1.5, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
                }
            }
        });
    });

    // --- PROJECT MODALS LOGIC ---
    const modal = document.getElementById('project-modal');
    const modalBackdrop = modal.querySelector('.modal-backdrop');
    const modalContent = modal.querySelector('.modal-content');
    const closeBtn = modal.querySelector('.modal-close');
    
    // Modal Elements to inject data
    const mTitle = document.getElementById('modal-title');
    const mSubtitle = document.getElementById('modal-subtitle');
    const mDesc = document.getElementById('modal-desc');
    const mTags = document.getElementById('modal-tags');
    const mActions = document.getElementById('modal-actions');

    const openModal = (projectId) => {
        const data = projectsData[projectId];
        if(!data) return;

        // Inject Data
        mTitle.textContent = data.title;
        mSubtitle.textContent = data.subtitle;
        mDesc.innerHTML = data.description;
        
        mTags.innerHTML = '';
        data.tags.forEach(tag => {
            const span = document.createElement('span');
            span.className = 'tech-badge';
            span.style.padding = '0.4rem 1rem';
            span.style.fontSize = '0.75rem';
            span.textContent = tag;
            mTags.appendChild(span);
        });

        mActions.innerHTML = '';
        if(data.demo) {
            mActions.innerHTML += `<a href="${data.demo}" target="_blank" rel="noopener noreferrer" class="btn btn-primary magnetic-btn"><span class="magnetic-text">Demo ↗</span></a>`;
        }
        if(data.github) {
            mActions.innerHTML += `<a href="${data.github}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary magnetic-btn"><span class="magnetic-text">Código ↗</span></a>`;
        }

        // Apply new magnetic listeners to dynamically injected buttons
        const newMagnets = mActions.querySelectorAll('.magnetic-btn');
        newMagnets.forEach(btn => {
            btn.addEventListener('mousemove', function(e) {
                const rect = btn.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                const x = (e.clientX - centerX) * 0.15;
                const y = (e.clientY - centerY) * 0.15;
                gsap.to(btn, { x: x, y: y, duration: 0.5, ease: "power2.out" });
                const text = btn.querySelector('.magnetic-text');
                if(text) gsap.to(text, { x: x * 0.5, y: y * 0.5, duration: 0.5, ease: "power2.out" });
            });
            btn.addEventListener('mouseleave', function(e) {
                gsap.to(btn, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.3)" });
                const text = btn.querySelector('.magnetic-text');
                if(text) gsap.to(text, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1, 0.3)" });
            });
        });

        // Display and Animate IN
        modal.classList.add('open');

        // Reset scroll position AFTER display: flex
        const scrollArea = modal.querySelector('.modal-scroll-area');
        if(scrollArea) scrollArea.scrollTop = 0;

        gsap.to(modalBackdrop, { opacity: 1, duration: 0.4, ease: "power2.out" });
        gsap.to(modalContent, { opacity: 1, scale: 1, y: 0, duration: 0.5, ease: "back.out(1.2)", delay: 0.1 });
    };

    const closeModal = () => {
        // Animate OUT
        gsap.to(modalContent, { opacity: 0, scale: 0.95, y: 20, duration: 0.3, ease: "power2.in" });
        gsap.to(modalBackdrop, { opacity: 0, duration: 0.4, ease: "power2.in", delay: 0.1, onComplete: () => {
            modal.classList.remove('open');
        }});
    };

    // Attach click events to project cards
    document.querySelectorAll('.project-interactive').forEach(card => {
        card.addEventListener('click', (e) => {
            // Prevent click if they clicked on a link (if there were any inside)
            if(e.target.tagName.toLowerCase() === 'a') return;
            const projectId = card.getAttribute('data-project');
            openModal(projectId);
        });
    });

    closeBtn.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', closeModal);
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if(e.key === 'Escape' && modal.classList.contains('open')) {
            closeModal();
        }
    });

});
