import re

# --- 1. UPDATE STYLE.CSS ---
with open('/home/arkadain/portfolio/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add Spotlight CSS to .project-card
css = css.replace('.project-card {\n  background-color: var(--bg-card);', 
""".project-card {
  background-color: var(--bg-card);
  position: relative;""")

css = css.replace('.project-card:hover {\n  transform: translateY(-8px);',
""".project-card::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  border-radius: inherit;
  padding: 1px;
  background: radial-gradient(
    600px circle at var(--mouse-x, 0) var(--mouse-y, 0),
    rgba(255,255,255,0.15),
    transparent 40%
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.5s;
  pointer-events: none;
  z-index: 10;
}

.project-card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(
    600px circle at var(--mouse-x, 0) var(--mouse-y, 0),
    rgba(255,255,255,0.03),
    transparent 40%
  );
  opacity: 0;
  transition: opacity 0.5s;
  pointer-events: none;
  z-index: 0;
}

.project-card:hover::before,
.project-card:hover::after {
  opacity: 1;
}

.project-image, .project-content {
  position: relative;
  z-index: 2;
}

.project-card:hover {""")

# Staggered reveal for project cards
css = css.replace('.project-card {', 
""".project-card {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.3s, border-color 0.3s;
""")

css = css.replace('.project-card:hover {\n  transform: translateY(-8px);',
""".project-card.visible {
  opacity: 1;
  transform: translateY(0);
}

.project-card:hover {
  transform: translateY(-8px);""")

# Magnetic Button Classes
magnetic_css = """
/* Magnetic Button */
.btn-magnetic {
  position: relative;
  transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1), background-color 0.3s, box-shadow 0.3s;
}
.btn-magnetic-text {
  display: inline-block;
  pointer-events: none;
  transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
}
"""
if "btn-magnetic" not in css:
    css += magnetic_css

with open('/home/arkadain/portfolio/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# --- 2. UPDATE MAIN.JS ---
with open('/home/arkadain/portfolio/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add spotlight listener and magnetic buttons
new_js_logic = """
    // Staggered reveal for project cards
    const cardObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add stagger delay based on DOM order
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px' });
    
    document.querySelectorAll('.project-card').forEach(card => {
        cardObserver.observe(card);
    });

    // Spotlight effect for cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // Magnetic Buttons
    const magnets = document.querySelectorAll('.btn-magnetic');
    magnets.forEach(btn => {
        btn.addEventListener('mousemove', function(e) {
            const position = btn.getBoundingClientRect();
            const x = e.pageX - position.left - position.width / 2;
            const y = e.pageY - position.top - position.height / 2;
            
            // Move button slightly
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.5}px)`;
            
            // Move text inside slightly more for 3D effect
            const text = btn.querySelector('.btn-magnetic-text');
            if(text) text.style.transform = `translate(${x * 0.2}px, ${y * 0.3}px)`;
        });

        btn.addEventListener('mouseout', function(e) {
            btn.style.transform = 'translate(0px, 0px)';
            const text = btn.querySelector('.btn-magnetic-text');
            if(text) text.style.transform = 'translate(0px, 0px)';
        });
    });
"""

if "Spotlight effect" not in js:
    # Insert before the end of DOMContentLoaded
    js = js.replace('});\n', new_js_logic + '});\n', 1)

with open('/home/arkadain/portfolio/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Animation updates applied.")
