from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib

# Load AI model
print("Loading AI model...")
try:
    model = joblib.load('models/loan_prediction_model.pkl')
    feature_names = joblib.load('models/feature_names.pkl')
    print("AI model loaded successfully!")
except:
    print("Could not load AI model - check if models folder exists")
    model = None
    feature_names = None

app = FastAPI(title="CreditAI Professional")

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>CreditAI - Advanced Assessment Platform</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background: #000;
            color: white;
            line-height: 1.6;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Advanced layered background system */
        .bg-layer-1 {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -5;
            background: radial-gradient(ellipse at center, #0f0f23 0%, #000 70%);
        }
        
        .bg-layer-2 {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -4;
            background: 
                radial-gradient(circle at 20% 20%, rgba(102, 126, 234, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.12) 0%, transparent 50%),
                radial-gradient(circle at 40% 60%, rgba(56, 178, 172, 0.08) 0%, transparent 50%);
            animation: bgFloat 20s ease-in-out infinite alternate;
        }
        
        .bg-layer-3 {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            opacity: 0.03;
            background-image: 
                linear-gradient(30deg, transparent 49%, rgba(255,255,255,0.1) 50%, transparent 51%),
                linear-gradient(150deg, transparent 49%, rgba(255,255,255,0.05) 50%, transparent 51%);
            background-size: 60px 60px;
            animation: bgShift 40s linear infinite;
        }
        
        @keyframes bgFloat {
            0% { transform: scale(1) rotate(0deg); opacity: 0.6; }
            50% { transform: scale(1.1) rotate(1deg); opacity: 0.8; }
            100% { transform: scale(1.05) rotate(-1deg); opacity: 0.7; }
        }
        
        @keyframes bgShift {
            0% { transform: translateX(0) translateY(0); }
            100% { transform: translateX(-60px) translateY(-60px); }
        }
        
        /* Floating particles system */
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            pointer-events: none;
        }
        
        .particle {
            position: absolute;
            width: 2px;
            height: 2px;
            background: rgba(102, 126, 234, 0.6);
            border-radius: 50%;
            animation: float 25s infinite linear;
        }
        
        .particle:nth-child(odd) { background: rgba(118, 75, 162, 0.4); }
        .particle:nth-child(1) { left: 10%; animation-delay: 0s; animation-duration: 20s; }
        .particle:nth-child(2) { left: 20%; animation-delay: 3s; animation-duration: 25s; }
        .particle:nth-child(3) { left: 30%; animation-delay: 6s; animation-duration: 22s; }
        .particle:nth-child(4) { left: 40%; animation-delay: 9s; animation-duration: 28s; }
        .particle:nth-child(5) { left: 50%; animation-delay: 12s; animation-duration: 24s; }
        .particle:nth-child(6) { left: 60%; animation-delay: 15s; animation-duration: 26s; }
        .particle:nth-child(7) { left: 70%; animation-delay: 18s; animation-duration: 23s; }
        .particle:nth-child(8) { left: 80%; animation-delay: 21s; animation-duration: 27s; }
        .particle:nth-child(9) { left: 90%; animation-delay: 24s; animation-duration: 21s; }
        
        @keyframes float {
            0% { 
                transform: translateY(100vh) scale(0);
                opacity: 0;
            }
            10% { 
                transform: translateY(90vh) scale(1);
                opacity: 1;
            }
            90% { 
                transform: translateY(-10vh) scale(1);
                opacity: 0.8;
            }
            100% { 
                transform: translateY(-20vh) scale(0);
                opacity: 0;
            }
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            position: relative;
            z-index: 1;
        }
        
        /* Advanced hero section with depth */
        .hero {
            text-align: center;
            padding: 100px 0 80px 0;
            position: relative;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 800px;
            height: 400px;
            background: radial-gradient(ellipse, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
            filter: blur(40px);
            z-index: -1;
            animation: heroGlow 8s ease-in-out infinite alternate;
        }
        
        @keyframes heroGlow {
            0% { opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }
            100% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.2); }
        }
        
        .logo {
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 30%, #f093fb 60%, #667eea 100%);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 30px;
            letter-spacing: -3px;
            position: relative;
            animation: gradientShift 6s ease-in-out infinite;
            filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.3));
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .logo::after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #667eea, transparent);
            animation: lineGlow 3s ease-in-out infinite alternate;
        }
        
        @keyframes lineGlow {
            0% { opacity: 0.4; width: 60px; }
            100% { opacity: 1; width: 100px; }
        }
        
        .hero-title {
            font-size: 4.2rem;
            font-weight: 700;
            margin-bottom: 30px;
            background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 50%, #ffffff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
            letter-spacing: -2px;
            position: relative;
            overflow: hidden;
        }
        
        .hero-title::after {
            content: '';
            position: absolute;
            right: 0;
            top: 0;
            height: 100%;
            width: 3px;
            background: #667eea;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
        
        .hero-subtitle {
            font-size: 1.4rem;
            color: rgba(255, 255, 255, 0.7);
            max-width: 700px;
            margin: 0 auto 60px;
            font-weight: 400;
            line-height: 1.6;
        }
        
        /* Enhanced main card with multiple layers */
        .main-card {
            background: rgba(10, 10, 20, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 32px;
            padding: 80px;
            margin: 80px 0;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                0 16px 64px rgba(0, 0, 0, 0.2),
                0 32px 128px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        
        .main-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.6), rgba(118, 75, 162, 0.4), transparent);
            animation: borderGlow 4s ease-in-out infinite alternate;
        }
        
        @keyframes borderGlow {
            0% { opacity: 0.3; }
            100% { opacity: 1; }
        }
        
        .main-card::after {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, 
                rgba(102, 126, 234, 0.1) 0%, 
                transparent 25%, 
                transparent 50%,
                rgba(118, 75, 162, 0.1) 75%,
                transparent 100%);
            border-radius: 32px;
            z-index: -1;
            animation: cardGlow 8s ease-in-out infinite;
        }
        
        @keyframes cardGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        /* Enhanced form sections with staggered reveals */
        .form-section {
            margin-bottom: 70px;
            position: relative;
            opacity: 0;
            transform: translateY(50px);
            animation: sectionReveal 0.8s ease-out forwards;
        }
        
        .form-section:nth-child(1) { animation-delay: 0.1s; }
        .form-section:nth-child(2) { animation-delay: 0.3s; }
        .form-section:nth-child(3) { animation-delay: 0.5s; }
        
        @keyframes sectionReveal {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .section-title {
            font-size: 1.8rem;
            font-weight: 600;
            color: white;
            margin-bottom: 45px;
            padding-left: 30px;
            position: relative;
            display: flex;
            align-items: center;
        }
        
        .section-title::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 4px;
            height: 32px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 3px;
            box-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
        }
        
        .section-title::after {
            content: '';
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, rgba(102, 126, 234, 0.3) 0%, transparent 100%);
            margin-left: 30px;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 40px;
        }
        
        /* Input field focus animation with ripple effect */
        .input-group {
            position: relative;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .input-group::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: all 0.4s ease;
            z-index: 0;
            pointer-events: none;
        }
        
        .input-group:focus-within::before {
            width: 120%;
            height: 120%;
        }
        
        .input-group:hover {
            transform: translateY(-3px);
        }
        
        .input-label {
            display: block;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 20px;
            font-size: 0.85rem;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            position: relative;
        }
        
        .input-field {
            width: 100%;
            padding: 24px 28px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            color: white;
            font-size: 16px;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 400;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            z-index: 1;
            box-shadow: 
                0 4px 20px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                inset 0 -1px 0 rgba(0, 0, 0, 0.1);
        }
        
        .input-field:focus {
            outline: none;
            border-color: rgba(102, 126, 234, 0.6);
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 
                0 0 0 3px rgba(102, 126, 234, 0.1),
                0 8px 32px rgba(102, 126, 234, 0.15),
                0 4px 20px rgba(0, 0, 0, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            transform: translateY(-4px);
        }
        
        .input-field::placeholder {
            color: rgba(255, 255, 255, 0.35);
            font-weight: 300;
        }
        
        /* Premium stats section */
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            margin: 80px 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 24px;
            padding: 40px 30px;
            text-align: center;
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.03), transparent);
            transition: left 1s;
        }
        
        .stat-card:hover::before {
            left: 100%;
        }
        
        .stat-card:hover {
            transform: translateY(-10px) scale(1.02);
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(102, 126, 234, 0.3);
            box-shadow: 
                0 20px 60px rgba(102, 126, 234, 0.15),
                0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        /* Stats numbers with no pulsing effects */
        .stat-number {
            font-size: 2.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.3));
        }
        
        .stat-label {
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
            font-size: 1rem;
            letter-spacing: 0.5px;
        }
        
        /* Submit button with advanced tech effects */
        .submit-section {
            text-align: center;
            margin-top: 80px;
            padding-top: 50px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            position: relative;
        }
        
        .submit-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.6), transparent);
        }
        
        .submit-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 200% 200%;
            color: white;
            border: none;
            padding: 24px 60px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 50px;
            cursor: pointer;
            font-family: 'Space Grotesk', sans-serif;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 8px 32px rgba(102, 126, 234, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
            letter-spacing: 1px;
            text-transform: uppercase;
            animation: gradientShift 8s ease-in-out infinite;
        }
        
        /* Pulse ring effect on button */
        .submit-btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(102, 126, 234, 0.4);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: all 0.6s ease;
        }
        
        .submit-btn:hover::before {
            width: 300px;
            height: 300px;
            background: rgba(102, 126, 234, 0.1);
        }
        
        /* Scanning line effect */
        .submit-btn::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.8s ease;
        }
        
        .submit-btn:hover::after {
            left: 100%;
        }
        
        .submit-btn:hover {
            transform: translateY(-6px) scale(1.02);
            box-shadow: 
                0 16px 48px rgba(102, 126, 234, 0.4),
                0 8px 32px rgba(118, 75, 162, 0.2),
                0 0 80px rgba(102, 126, 234, 0.1);
            background-position: 100% 0;
        }
        
        .submit-btn:active {
            transform: translateY(-3px) scale(0.98);
        }
        
        /* Button loading state with morphing effect */
        .submit-btn.loading {
            pointer-events: none;
            background: linear-gradient(135deg, #4a5568, #2d3748);
            animation: buttonLoading 2s ease-in-out infinite;
        }
        
        @keyframes buttonLoading {
            0%, 100% { 
                transform: scale(1);
                box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
            }
            50% { 
                transform: scale(1.02);
                box-shadow: 0 12px 48px rgba(102, 126, 234, 0.5);
            }
        }
        
        /* Advanced loading state with techy animations */
        .loading {
            display: none;
            text-align: center;
            margin-top: 50px;
            animation: loadingAppear 0.5s ease;
        }
        
        .loading.show { 
            display: block; 
        }
        
        @keyframes loadingAppear {
            0% { opacity: 0; transform: scale(0.8) translateY(20px); }
            100% { opacity: 1; transform: scale(1) translateY(0); }
        }
        
        /* Epic tech-style spinner with multiple rings */
        .spinner-container {
            position: relative;
            width: 80px;
            height: 80px;
            margin: 0 auto 30px;
        }
        
        .spinner {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 2px solid transparent;
            border-radius: 50%;
            animation: spin 2s linear infinite;
        }
        
        .spinner:nth-child(1) {
            border-top: 2px solid #667eea;
            border-right: 2px solid #667eea;
            animation-duration: 2s;
        }
        
        .spinner:nth-child(2) {
            border-bottom: 2px solid #764ba2;
            border-left: 2px solid #764ba2;
            width: 60px;
            height: 60px;
            top: 10px;
            left: 10px;
            animation-duration: 1.5s;
            animation-direction: reverse;
        }
        
        .spinner:nth-child(3) {
            border-top: 2px solid #f093fb;
            width: 40px;
            height: 40px;
            top: 20px;
            left: 20px;
            animation-duration: 1s;
        }
        
        /* Loading dots animation */
        .loading-dots {
            margin-top: 20px;
        }
        
        .dot {
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #667eea;
            border-radius: 50%;
            margin: 0 3px;
            animation: dotPulse 1.5s infinite ease-in-out;
        }
        
        .dot:nth-child(1) { animation-delay: 0s; }
        .dot:nth-child(2) { animation-delay: 0.2s; background: #764ba2; }
        .dot:nth-child(3) { animation-delay: 0.4s; background: #f093fb; }
        
        @keyframes dotPulse {
            0%, 60%, 100% { 
                transform: scale(1);
                opacity: 0.7; 
            }
            30% { 
                transform: scale(1.3);
                opacity: 1; 
            }
        }
        
        /* Progress bar animation */
        .progress-container {
            width: 300px;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
            margin: 25px auto;
            overflow: hidden;
            position: relative;
        }
        
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            border-radius: 2px;
            width: 0%;
            animation: progressFill 3s ease-in-out infinite;
            position: relative;
        }
        
        .progress-bar::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shimmer 1.5s infinite;
        }
        
        @keyframes progressFill {
            0% { width: 0%; }
            50% { width: 70%; }
            100% { width: 100%; }
        }
        
        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .hero-title { font-size: 3rem; }
            .main-card { 
                padding: 50px 30px; 
                margin: 50px 0; 
            }
            .form-grid { 
                grid-template-columns: 1fr; 
                gap: 30px;
            }
            .container { padding: 0 15px; }
            .hero { padding: 60px 0 50px 0; }
            .stats { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
</head>
<body>
    <!-- Multi-layered background system -->
    <div class="bg-layer-1"></div>
    <div class="bg-layer-2"></div>
    <div class="bg-layer-3"></div>
    
    <!-- Floating particle system -->
    <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>
    
    <div class="container">
        <section class="hero">
            <div class="logo">CreditAI</div>
            <h1 class="hero-title">Advanced Assessment Platform</h1>
            <p class="hero-subtitle">Next-generation AI technology analyzes Indonesian SME data with unprecedented 90.5% accuracy for instant, intelligent loan decisions</p>
        </section>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">90.5%</div>
                <div class="stat-label">AI Precision</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">&lt;2s</div>
                <div class="stat-label">Analysis Speed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">1000+</div>
                <div class="stat-label">Profiles Analyzed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">12</div>
                <div class="stat-label">Data Variables</div>
            </div>
        </div>
        
        <div class="main-card">
            <form action="/predict" method="post" onsubmit="showLoading()">
                <div class="form-section">
                    <h2 class="section-title">Business Profile</h2>
                    <div class="form-grid">
                        <div class="input-group">
                            <label class="input-label">Business Name</label>
                            <input type="text" name="business_name" class="input-field" placeholder="Enter your business name" required>
                        </div>
                        <div class="input-group">
                            <label class="input-label">Owner Age</label>
                            <input type="number" name="owner_age" class="input-field" placeholder="35" min="18" max="80" required>
                        </div>
                    </div>
                    <div class="form-grid">
                        <div class="input-group">
                            <label class="input-label">Years in Business</label>
                            <input type="number" name="years_in_business" class="input-field" placeholder="5" min="0" max="50" required>
                        </div>
                        <div class="input-group">
                            <label class="input-label">Number of Employees</label>
                            <input type="number" name="employee_count" class="input-field" placeholder="8" min="1" max="100" required>
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h2 class="section-title">Digital Presence</h2>
                    <div class="form-grid">
                        <div class="input-group">
                            <label class="input-label">Instagram Followers</label>
                            <input type="number" name="instagram_followers" class="input-field" placeholder="2500" min="0" value="0">
                        </div>
                        <div class="input-group">
                            <label class="input-label">Tokopedia Rating</label>
                            <input type="number" name="tokopedia_rating" class="input-field" placeholder="4.5" min="0" max="5" step="0.1" value="0">
                        </div>
                    </div>
                    <div class="input-group">
                        <label class="input-label">Monthly Digital Transactions</label>
                        <input type="number" name="monthly_digital_payments" class="input-field" placeholder="180" min="0" required>
                    </div>
                </div>
                
                <div class="form-section">
                    <h2 class="section-title">Financial Overview</h2>
                    <div class="form-grid">
                        <div class="input-group">
                            <label class="input-label">Monthly Revenue (IDR)</label>
                            <input type="number" name="monthly_revenue" class="input-field" placeholder="75000000" min="0" required>
                        </div>
                        <div class="input-group">
                            <label class="input-label">Loan Amount Requested (IDR)</label>
                            <input type="number" name="loan_amount_requested" class="input-field" placeholder="150000000" min="0" required>
                        </div>
                    </div>
                </div>
                
                <div class="loading" id="loading">
                    <div class="spinner-container">
                        <div class="spinner"></div>
                        <div class="spinner"></div>
                        <div class="spinner"></div>
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar"></div>
                    </div>
                    <p style="color: #667eea; font-weight: 500; font-size: 1.1rem; margin-bottom: 10px;">Advanced AI analyzing business profile...</p>
                    <div class="loading-dots">
                        <span class="dot"></span>
                        <span class="dot"></span>
                        <span class="dot"></span>
                    </div>
                </div>
                
                <div class="submit-section">
                    <button type="submit" class="submit-btn" id="submitBtn">
                        Launch Assessment
                    </button>
                </div>
            </form>
        </div>
    </div>
    
    <script>
        function showLoading() {
            const loading = document.getElementById('loading');
            const submitBtn = document.getElementById('submitBtn');
            
            // Add loading class to button for morphing effect
            submitBtn.classList.add('loading');
            submitBtn.textContent = 'ANALYZING...';
            
            // Show loading animation
            loading.classList.add('show');
            
            // Hide button after delay
            setTimeout(() => {
                submitBtn.style.display = 'none';
            }, 500);
        }
        
        // Enhanced interactive effects with modern animations
        document.addEventListener('DOMContentLoaded', function() {
            // Stagger form section animations
            const sections = document.querySelectorAll('.form-section');
            sections.forEach((section, index) => {
                section.style.animationDelay = (index * 0.2) + 's';
            });
            
            // Enhanced input interactions with ripple effect
            document.querySelectorAll('.input-field').forEach(input => {
                input.addEventListener('focus', function() {
                    this.parentElement.style.transform = 'translateY(-2px) scale(1.01)';
                    this.parentElement.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
                });
                
                input.addEventListener('blur', function() {
                    this.parentElement.style.transform = 'translateY(0) scale(1)';
                });
                
                // Typing effect
                input.addEventListener('input', function() {
                    this.style.transform = 'scale(1.005)';
                    setTimeout(() => {
                        this.style.transform = 'scale(1)';
                    }, 100);
                });
            });
            
            // Animate stat numbers counting up
            const statNumbers = document.querySelectorAll('.stat-number');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const text = target.textContent;
                        
                        if (text.includes('%')) {
                            animateNumber(target, 0, 90.5, '%');
                        } else if (text.includes('s')) {
                            animateNumber(target, 0, 2, 's');
                        } else if (text.includes('+')) {
                            animateNumber(target, 0, 1000, '+');
                        } else if (!isNaN(text)) {
                            animateNumber(target, 0, parseInt(text), '');
                        }
                    }
                });
            });
            
            statNumbers.forEach(stat => observer.observe(stat));
            
            function animateNumber(element, start, end, suffix) {
                let current = start;
                const increment = (end - start) / 60; // 60 frames
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= end) {
                        current = end;
                        clearInterval(timer);
                    }
                    
                    if (suffix === '%') {
                        element.textContent = current.toFixed(1) + suffix;
                    } else if (suffix === 's') {
                        element.textContent = '<' + Math.ceil(current) + suffix;
                    } else if (suffix === '+') {
                        element.textContent = Math.floor(current) + suffix;
                    } else {
                        element.textContent = Math.floor(current);
                    }
                }, 16);
            }
            
            // Add particle effect on button hover
            const submitBtn = document.getElementById('submitBtn');
            if (submitBtn) {
                submitBtn.addEventListener('mouseenter', function() {
                    createParticles(this);
                });
            }
            
            function createParticles(button) {
                for (let i = 0; i < 6; i++) {
                    setTimeout(() => {
                        const particle = document.createElement('div');
                        particle.style.cssText = `
                            position: absolute;
                            width: 4px;
                            height: 4px;
                            background: #667eea;
                            border-radius: 50%;
                            pointer-events: none;
                            z-index: 1000;
                        `;
                        
                        const rect = button.getBoundingClientRect();
                        particle.style.left = (rect.left + Math.random() * rect.width) + 'px';
                        particle.style.top = (rect.top + Math.random() * rect.height) + 'px';
                        
                        document.body.appendChild(particle);
                        
                        // Animate particle
                        const animation = particle.animate([
                            { 
                                transform: 'translate(0, 0) scale(1)', 
                                opacity: 1 
                            },
                            { 
                                transform: `translate(${(Math.random() - 0.5) * 100}px, ${-50 - Math.random() * 50}px) scale(0)`, 
                                opacity: 0 
                            }
                        ], {
                            duration: 800,
                            easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
                        });
                        
                        animation.onfinish = () => particle.remove();
                    }, i * 100);
                }
            }
        });
    </script>
</body>
</html>
    '''
    return HTMLResponse(content=html_content)

@app.post("/predict", response_class=HTMLResponse)
async def predict_loan(
    business_name: str = Form(...),
    owner_age: int = Form(...),
    years_in_business: int = Form(...),
    employee_count: int = Form(...),
    instagram_followers: int = Form(0),
    tokopedia_rating: float = Form(0.0),
    monthly_digital_payments: int = Form(...),
    monthly_revenue: int = Form(...),
    loan_amount_requested: int = Form(...)
):
    if model is None:
        return HTMLResponse(content="<h1>Error: AI model not loaded</h1>")
    
    # Prepare data
    has_instagram_num = 1 if instagram_followers > 0 else 0
    has_tokopedia_num = 1 if tokopedia_rating > 0 else 0
    revenue_to_loan_ratio = monthly_revenue / loan_amount_requested if loan_amount_requested > 0 else 0
    
    digital_presence_score = (
        has_instagram_num * 0.3 + 
        has_tokopedia_num * 0.3 + 
        (1 if instagram_followers > 1000 else 0) * 0.2 +
        (1 if tokopedia_rating > 4.0 else 0) * 0.2
    )
    
    # Features array
    features = [
        owner_age, years_in_business, employee_count,
        has_instagram_num, instagram_followers, has_tokopedia_num,
        tokopedia_rating, monthly_digital_payments, monthly_revenue,
        loan_amount_requested, revenue_to_loan_ratio, digital_presence_score
    ]
    
    # Prediction
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0]
    approval_probability = probability[1] * 100
    
    # Status - NO COLORS OR ICONS, just text
    if approval_probability > 75:
        status_text = "APPROVED"
        recommendation = "Excellent candidate - recommended for immediate approval"
    elif approval_probability > 50:
        status_text = "UNDER REVIEW"
        recommendation = "Moderate risk - additional documentation recommended"
    else:
        status_text = "DECLINED"
        recommendation = "High risk assessment - requires additional collateral"
    
    result_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>CreditAI - Assessment Results</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Space Grotesk', sans-serif;
            background: #000;
            color: white;
            margin: 0;
            overflow-x: hidden;
            position: relative;
        }}
        
        /* Consistent blue background - NO status colors */
        .bg-layer-1 {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -3;
            background: radial-gradient(ellipse at center, #0f0f23 0%, #000 70%);
        }}
        
        .bg-layer-2 {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            background: 
                radial-gradient(circle at 30% 20%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 70% 80%, rgba(102, 126, 234, 0.08) 0%, transparent 50%);
            animation: resultBgFloat 15s ease-in-out infinite alternate;
        }}
        
        @keyframes resultBgFloat {{
            0% {{ transform: scale(1) rotate(0deg); opacity: 0.6; }}
            100% {{ transform: scale(1.1) rotate(2deg); opacity: 0.9; }}
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 60px 20px;
            position: relative;
            z-index: 1;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 60px;
            position: relative;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 600px;
            height: 300px;
            background: radial-gradient(ellipse, rgba(102, 126, 234, 0.08) 0%, transparent 70%);
            filter: blur(60px);
            z-index: -1;
            animation: headerGlow 6s ease-in-out infinite alternate;
        }}
        
        @keyframes headerGlow {{
            0% {{ opacity: 0.4; transform: translate(-50%, -50%) scale(0.8); }}
            100% {{ opacity: 0.8; transform: translate(-50%, -50%) scale(1.2); }}
        }}
        
        .logo {{
            font-size: 2.4rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            letter-spacing: -1px;
        }}
        
        .business-name {{
            font-size: 3rem;
            font-weight: 600;
            color: white;
            margin-bottom: 15px;
            animation: titleSlide 0.8s ease-out;
        }}
        
        @keyframes titleSlide {{
            0% {{ opacity: 0; transform: translateY(-20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .subtitle {{
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.2rem;
            margin-bottom: 40px;
        }}
        
        /* Result card with consistent blue theme */
        .result-card {{
            background: rgba(10, 10, 20, 0.9);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 32px;
            padding: 70px;
            margin: 50px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 20px 80px rgba(0, 0, 0, 0.4),
                0 8px 32px rgba(0, 0, 0, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            animation: cardAppear 1s ease-out;
        }}
        
        @keyframes cardAppear {{
            0% {{ opacity: 0; transform: scale(0.95) translateY(30px); }}
            100% {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}
        
        .result-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #667eea, transparent);
            animation: topBorderGlow 3s ease-in-out infinite alternate;
        }}
        
        @keyframes topBorderGlow {{
            0% {{ opacity: 0.5; }}
            100% {{ opacity: 1; }}
        }}
        
        .result-card::after {{
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(135deg, 
                rgba(102, 126, 234, 0.05) 0%, 
                transparent 30%, 
                transparent 70%, 
                rgba(118, 75, 162, 0.05) 100%);
            border-radius: 32px;
            z-index: -1;
            animation: cardBorderGlow 5s ease-in-out infinite;
        }}
        
        @keyframes cardBorderGlow {{
            0%, 100% {{ opacity: 0.6; }}
            50% {{ opacity: 1; }}
        }}
        
        /* Percentage always blue */
        .probability {{
            font-size: 5rem;
            font-weight: 800;
            color: #667eea;
            margin-bottom: 25px;
            position: relative;
            animation: numberCount 2s ease-out 0.8s both;
            filter: drop-shadow(0 0 30px rgba(102, 126, 234, 0.6));
        }}
        
        @keyframes numberCount {{
            0% {{ transform: scale(0.5); opacity: 0; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        
        .probability::after {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: radial-gradient(circle, rgba(102, 126, 234, 0.08) 0%, transparent 70%);
            transform: translate(-50%, -50%);
            z-index: -1;
            animation: probabilityGlow 4s ease-in-out infinite;
        }}
        
        @keyframes probabilityGlow {{
            0%, 100% {{ opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }}
            50% {{ opacity: 0.7; transform: translate(-50%, -50%) scale(1.2); }}
        }}
        
        /* Status text always blue */
        .status {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 25px;
            letter-spacing: 3px;
            animation: statusSlide 0.8s ease-out 1.2s both;
        }}
        
        @keyframes statusSlide {{
            0% {{ opacity: 0; transform: translateX(-50px); }}
            100% {{ opacity: 1; transform: translateX(0); }}
        }}
        
        .recommendation {{
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.85);
            margin-bottom: 50px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
            animation: recommendationFade 1s ease-out 1.5s both;
        }}
        
        @keyframes recommendationFade {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        
        /* Enhanced details section */
        .details {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin: 60px 0;
            animation: detailsSlide 1s ease-out 1.8s both;
        }}
        
        @keyframes detailsSlide {{
            0% {{ opacity: 0; transform: translateY(30px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .detail {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px 25px;
            text-align: center;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .detail::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
            transition: left 1s;
        }}
        
        .detail:hover::before {{
            left: 100%;
        }}
        
        .detail:hover {{
            transform: translateY(-8px) scale(1.02);
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(102, 126, 234, 0.4);
            box-shadow: 0 15px 40px rgba(102, 126, 234, 0.15);
        }}
        
        .detail-label {{
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.6);
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 500;
        }}
        
        .detail-value {{
            font-size: 1.4rem;
            font-weight: 600;
            color: white;
        }}
        
        /* Action button */
        .actions {{
            text-align: center;
            margin-top: 60px;
            animation: actionsAppear 1s ease-out 2s both;
        }}
        
        @keyframes actionsAppear {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        
        .btn {{
            display: inline-block;
            padding: 18px 36px;
            margin: 0 15px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-family: 'Space Grotesk', sans-serif;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 1rem;
            position: relative;
            overflow: hidden;
            letter-spacing: 0.5px;
        }}
        
        .btn::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.6s;
        }}
        
        .btn:hover::before {{
            left: 100%;
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        }}
        
        .btn:hover {{
            transform: translateY(-4px) scale(1.02);
        }}
        
        .btn-primary:hover {{
            box-shadow: 0 16px 48px rgba(102, 126, 234, 0.4);
        }}
        
        /* Responsive design */
        @media (max-width: 768px) {{
            .container {{ padding: 40px 15px; }}
            .result-card {{ padding: 50px 30px; }}
            .business-name {{ font-size: 2.2rem; }}
            .probability {{ font-size: 3.8rem; }}
            .status {{ font-size: 1.8rem; }}
            .details {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="bg-layer-1"></div>
    <div class="bg-layer-2"></div>
    
    <div class="container">
        <div class="header">
            <div class="logo">CreditAI</div>
            <h1 class="business-name">{business_name}</h1>
            <p class="subtitle">Assessment Analysis Complete</p>
        </div>
        
        <div class="result-card">
            <div class="probability">{approval_probability:.0f}%</div>
            <div class="status">{status_text}</div>
            <p class="recommendation">{recommendation}</p>
        </div>
        
        <div class="details">
            <div class="detail">
                <div class="detail-label">Monthly Revenue</div>
                <div class="detail-value">IDR {monthly_revenue:,}</div>
            </div>
            <div class="detail">
                <div class="detail-label">Loan Amount</div>
                <div class="detail-value">IDR {loan_amount_requested:,}</div>
            </div>
            <div class="detail">
                <div class="detail-label">Business Experience</div>
                <div class="detail-value">{years_in_business} {'Year' if years_in_business == 1 else 'Years'}</div>
            </div>
            <div class="detail">
                <div class="detail-label">Digital Presence</div>
                <div class="detail-value">{digital_presence_score:.1f}/1.0</div>
            </div>
        </div>
        
        <div class="actions">
            <a href="/" class="btn btn-primary">New Assessment</a>
        </div>
    </div>
    
    <script>
        // Advanced result page interactions
        document.addEventListener('DOMContentLoaded', function() {{
            // Animate probability number counting
            const probElement = document.querySelector('.probability');
            const finalValue = {approval_probability:.0f};
            let currentValue = 0;
            const duration = 2000;
            const increment = finalValue / (duration / 16);
            
            function updateCounter() {{
                currentValue += increment;
                if (currentValue >= finalValue) {{
                    currentValue = finalValue;
                    probElement.textContent = finalValue + '%';
                    return;
                }}
                probElement.textContent = Math.floor(currentValue) + '%';
                requestAnimationFrame(updateCounter);
            }}
            
            setTimeout(updateCounter, 800);
        }});
    </script>
</body>
</html>
    '''
    
    return HTMLResponse(content=result_html)

if __name__ == "__main__":
    import uvicorn
    print("Starting final clean CreditAI server...")
    print("Open your browser to: http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
