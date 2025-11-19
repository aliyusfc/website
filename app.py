from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} - Banking Professional</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        .navbar {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .nav-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }
        
        .logo {
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #ffd700;
        }
        
        .hero {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 150px 2rem 100px;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .cta-button {
            background: #ffd700;
            color: #1e3c72;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: transform 0.3s;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
        }
        
        .section {
            max-width: 1200px;
            margin: 0 auto;
            padding: 80px 2rem;
        }
        
        .section-title {
            font-size: 2.5rem;
            margin-bottom: 3rem;
            text-align: center;
            color: #1e3c72;
        }
        
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }
        
        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: #2a5298;
        }
        
        .about-text p {
            margin-bottom: 1rem;
            color: #555;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .stat-card {
            background: #f8f9fa;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            border-left: 4px solid #2a5298;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1e3c72;
        }
        
        .stat-label {
            color: #666;
            margin-top: 0.5rem;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .service-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
        }
        
        .service-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .service-card h3 {
            color: #1e3c72;
            margin-bottom: 1rem;
        }
        
        .experience-timeline {
            position: relative;
            padding-left: 3rem;
        }
        
        .timeline-item {
            margin-bottom: 3rem;
            position: relative;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -3rem;
            top: 0;
            width: 20px;
            height: 20px;
            background: #2a5298;
            border-radius: 50%;
            border: 4px solid white;
            box-shadow: 0 0 0 2px #2a5298;
        }
        
        .timeline-item::after {
            content: '';
            position: absolute;
            left: -2.55rem;
            top: 20px;
            width: 2px;
            height: calc(100% + 3rem);
            background: #e0e0e0;
        }
        
        .timeline-item:last-child::after {
            display: none;
        }
        
        .timeline-date {
            color: #2a5298;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        .timeline-title {
            font-size: 1.3rem;
            color: #1e3c72;
            margin-bottom: 0.5rem;
        }
        
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 500;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #2a5298;
        }
        
        .form-group textarea {
            resize: vertical;
            min-height: 150px;
        }
        
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        footer {
            background: #1e3c72;
            color: white;
            text-align: center;
            padding: 2rem;
        }
        
        @media (max-width: 768px) {
            .about-content {
                grid-template-columns: 1fr;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .nav-links {
                gap: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-content">
            <div class="logo">{{ name }}</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section id="home" class="hero">
        <h1>{{ name }}</h1>
        <p>{{ title }}</p>
        <a href="#contact" class="cta-button">Get In Touch</a>
    </section>

    <section id="about" class="section">
        <h2 class="section-title">About Me</h2>
        <div class="about-content">
            <div class="about-text">
                <h3>Banking Excellence & Strategic Vision</h3>
                <p>With over {{ years_experience }} years of experience in the banking sector, I specialize in financial strategy, risk management, and portfolio optimization. My approach combines deep industry knowledge with innovative solutions to help clients achieve their financial goals.</p>
                <p>I've successfully managed portfolios worth millions, advised on complex financial transactions, and built lasting relationships with high-net-worth clients and institutional partners.</p>
            </div>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{{ years_experience }}+</div>
                    <div class="stat-label">Years Experience</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">200+</div>
                    <div class="stat-label">Clients Served</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">$50M+</div>
                    <div class="stat-label">Assets Managed</div>
                </div>
            </div>
        </div>
    </section>

    <section id="services" class="section" style="background: #f8f9fa;">
        <h2 class="section-title">Services</h2>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">💼</div>
                <h3>Wealth Management</h3>
                <p>Comprehensive wealth planning and investment strategies tailored to your financial objectives and risk tolerance.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">📊</div>
                <h3>Portfolio Analysis</h3>
                <p>In-depth portfolio reviews and optimization to maximize returns while managing risk effectively.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🏦</div>
                <h3>Corporate Banking</h3>
                <p>Strategic financial solutions for businesses including credit facilities, treasury services, and trade finance.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">📈</div>
                <h3>Investment Advisory</h3>
                <p>Expert guidance on market opportunities, asset allocation, and investment strategies across various markets.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🛡️</div>
                <h3>Risk Management</h3>
                <p>Comprehensive risk assessment and mitigation strategies to protect your financial interests.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🤝</div>
                <h3>Financial Consulting</h3>
                <p>Strategic financial advice for mergers, acquisitions, and corporate restructuring initiatives.</p>
            </div>
        </div>
    </section>

    <section id="experience" class="section">
        <h2 class="section-title">Professional Experience</h2>
        <div class="experience-timeline">
            <div class="timeline-item">
                <div class="timeline-date">2020 - Present</div>
                <h3 class="timeline-title">Senior Vice President, Corporate Banking</h3>
                <p>Global Financial Services Inc.</p>
                <p>Leading a team of 15 professionals managing corporate relationships and credit portfolios exceeding $200M.</p>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2016 - 2020</div>
                <h3 class="timeline-title">Vice President, Private Banking</h3>
                <p>Premier Bank International</p>
                <p>Managed high-net-worth client relationships and developed customized investment strategies.</p>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2012 - 2016</div>
                <h3 class="timeline-title">Assistant Vice President, Investment Banking</h3>
                <p>Capital Markets Group</p>
                <p>Executed M&A transactions and provided financial advisory services to corporate clients.</p>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2008 - 2012</div>
                <h3 class="timeline-title">Financial Analyst</h3>
                <p>Standard Trust Bank</p>
                <p>Conducted financial analysis and supported senior bankers in deal execution and client management.</p>
            </div>
        </div>
    </section>

    <section id="contact" class="section" style="background: #f8f9fa;">
        <h2 class="section-title">Get In Touch</h2>
        {% if success %}
        <div class="success-message">
            Thank you for your message! I'll get back to you soon.
        </div>
        {% endif %}
        <form class="contact-form" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit" class="cta-button">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 {{ name }}. All rights reserved.</p>
        <p>Email: {{ email }} | Phone: {{ phone }}</p>
    </footer>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    success = False
    
    if request.method == 'POST':
        # Handle form submission
        success = True
        # In production, you could send email or save to database here
    
    # Portfolio data - customize these values
    data = {
        'name': 'Jonathan Williams',
        'title': 'Senior Banking Professional | Wealth Management Specialist',
        'years_experience': 15,
        'email': 'j.williams@banking.com',
        'phone': '+1 (555) 123-4567',
        'success': success
    }
    return render_template_string(template, **data)

# This is required for Vercel
app.debug = False