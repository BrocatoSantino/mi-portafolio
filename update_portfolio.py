import re

with open('/home/arkadain/portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #proyectos
proyectos_html = """        <!-- Proyectos -->
        <section id="proyectos" class="container">
            <h2>Trabajos Recientes</h2>
            <div class="projects-grid">
                <!-- Proyecto 1: TurnoFlow WhatsApp Bot -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800&auto=format&fit=crop" alt="Vista previa de TurnoFlow WhatsApp Bot">
                    </div>
                    <div class="project-content">
                        <h3>TurnoFlow WhatsApp Bot</h3>
                        <p>Sistema integral de reservas automatizado vía WhatsApp. SaaS Multi-Tenant para barberías con panel de administración y motor inteligente.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">Python</span>
                            <span class="tag">Supabase</span>
                            <span class="tag">SaaS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://github.com/BrocatoSantino/whatsapp-bot" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/whatsapp-bot" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- Proyecto 2: StudioArq -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop" alt="Vista previa de StudioArq">
                    </div>
                    <div class="project-content">
                        <h3>StudioArq</h3>
                        <p>Landing page inmersiva para estudio de arquitectura y diseño, con estética minimalista y animaciones suaves. Diseñando el futuro del espacio.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/StudioArq-landing/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/StudioArq-landing" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- Proyecto 3: NexaDigital -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800" alt="Vista previa de NexaDigital">
                    </div>
                    <div class="project-content">
                        <h3>NexaDigital</h3>
                        <p>Landing page corporativa de alta conversión para agencia de marketing digital. Construida con micro-animaciones al scroll y prueba social.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS v4</span>
                            <span class="tag">UX / Animaciones</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/nexadigital-landing-page/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/brocatosantino/nexadigital-landing-page" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>
            </div>
        </section>"""

# 2. Update #todos-los-trabajos
todos_html = """        <!-- Todos los trabajos -->
        <section id="todos-los-trabajos" class="container">
            <h2>Todos los Trabajos</h2>
            <div class="projects-grid">
                <!-- P1 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800&auto=format&fit=crop" alt="Vista previa de TurnoFlow WhatsApp Bot">
                    </div>
                    <div class="project-content">
                        <h3>TurnoFlow WhatsApp Bot</h3>
                        <p>Sistema integral de reservas automatizado vía WhatsApp. SaaS Multi-Tenant para barberías con panel de administración y motor inteligente.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">Python</span>
                            <span class="tag">Supabase</span>
                            <span class="tag">SaaS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://github.com/BrocatoSantino/whatsapp-bot" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/whatsapp-bot" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- P2 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=800&auto=format&fit=crop" alt="Vista previa de StudioArq">
                    </div>
                    <div class="project-content">
                        <h3>StudioArq</h3>
                        <p>Landing page inmersiva para estudio de arquitectura y diseño, con estética minimalista y animaciones suaves. Diseñando el futuro del espacio.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/StudioArq-landing/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/StudioArq-landing" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- P3 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=800&auto=format&fit=crop" alt="Vista previa de Cortes & Co.">
                    </div>
                    <div class="project-content">
                        <h3>Cortes & Co.</h3>
                        <p>Sitio web premium para barbería clásica con un diseño oscuro, elegante e interfaz tipo editorial de moda. Tu estilo, nuestra firma.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/CortesAndCo/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/CortesAndCo" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- P4 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop" alt="Vista previa de ServicioYa">
                    </div>
                    <div class="project-content">
                        <h3>ServicioYa</h3>
                        <p>Landing page de alta conversión para servicios de plomería y electricidad, enfocada en acción directa y confianza. Urgencias 24/7.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/ServicioYa-landing/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/BrocatoSantino/ServicioYa-landing" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- P5 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&q=80&w=800" alt="Vista previa de AURA Boutique">
                    </div>
                    <div class="project-content">
                        <h3>AURA Boutique</h3>
                        <p>Catálogo interactivo de tienda boutique estilo Apple. Cuenta con filtrado de productos por categoría y checkout directo por WhatsApp.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">Vanilla JS</span>
                            <span class="tag">TailwindCSS v4</span>
                            <span class="tag">E-Commerce</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/aura-boutique-catalog/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/brocatosantino/aura-boutique-catalog" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>

                <!-- P6 -->
                <article class="project-card">
                    <div class="project-image">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800" alt="Vista previa de NexaDigital">
                    </div>
                    <div class="project-content">
                        <h3>NexaDigital</h3>
                        <p>Landing page corporativa de alta conversión para agencia de marketing digital. Construida con micro-animaciones al scroll y prueba social.</p>
                        <div class="tags" style="margin-top: auto; margin-bottom: 1rem;">
                            <span class="tag">HTML5</span>
                            <span class="tag">TailwindCSS v4</span>
                            <span class="tag">UX / Animaciones</span>
                        </div>
                        <div style="display: flex; gap: 1.5rem;">
                            <a href="https://brocatosantino.github.io/nexadigital-landing-page/" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Proyecto</a>
                            <a href="https://github.com/brocatosantino/nexadigital-landing-page" target="_blank" rel="noopener noreferrer" class="project-link" style="margin-top: 0; padding-top: 0;">Ver Código</a>
                        </div>
                    </div>
                </article>
            </div>
        </section>"""

content = re.sub(r'<!-- Proyectos -->\s*<section id="proyectos" class="container">.*?</section>', proyectos_html, content, flags=re.DOTALL)
content = re.sub(r'<!-- Todos los trabajos -->\s*<section id="todos-los-trabajos" class="container">.*?</section>', todos_html, content, flags=re.DOTALL)

# Bump cache
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=20', content)

with open('/home/arkadain/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sections")
