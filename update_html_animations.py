import re

with open('/home/arkadain/portfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Buttons to use Magnetic class
# Replace <a href="..." class="btn btn-primary"> with <a href="..." class="btn btn-primary btn-magnetic"><span class="btn-magnetic-text">Enviar Email</span></a>
html = html.replace('class="btn btn-primary"', 'class="btn btn-primary btn-magnetic"')
html = html.replace('class="btn btn-secondary"', 'class="btn btn-secondary btn-magnetic"')

# We need to wrap the text inside the buttons with <span class="btn-magnetic-text">
html = re.sub(r'(<a[^>]*class="[^"]*btn-magnetic[^"]*"[^>]*>)\s*([^<]+)\s*</a>', r'\1<span class="btn-magnetic-text">\2</span></a>', html)

# 2. Text Masking Reveal on Hero h1
# Replace <h1>Santino Brocato<br>Desarrollador Web</h1>
# with a wrapped version for masking
hero_mask_html = """<h1 class="reveal-text">
                    <span class="reveal-mask"><span class="reveal-inner">Santino Brocato</span></span><br>
                    <span class="reveal-mask"><span class="reveal-inner" style="animation-delay: 0.2s">Desarrollador Web</span></span>
                </h1>"""
html = html.replace('<h1>Santino Brocato<br>Desarrollador Web</h1>', hero_mask_html)

# Bump cache version
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=21', html)
html = re.sub(r'main\.js\?v=\d+', 'main.js?v=21', html)

with open('/home/arkadain/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
