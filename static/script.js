// Real-time price ratio calculator
document.addEventListener('DOMContentLoaded', function() {
    // Only run on the detection page (index.html)
    if (document.querySelector('form')) {
        const originalPriceInput = document.querySelector('input[name="original_price"]');
        const discountedPriceInput = document.querySelector('input[name="discounted_price"]');
        
        // Calculate and display ratio in real-time
        function updateRatio() {
            const original = parseFloat(originalPriceInput.value);
            const discounted = parseFloat(discountedPriceInput.value);
            
            if (original && discounted && original > discounted) {
                const ratio = (original / discounted).toFixed(1);
                // Visual feedback
                discountedPriceInput.style.borderColor = 
                    ratio > 3 ? '#f39c12' : '#2ecc71';
            }
        }
        
        originalPriceInput.addEventListener('input', updateRatio);
        discountedPriceInput.addEventListener('input', updateRatio);
    }

    // Results page animations
    if (document.querySelector('.result-mode')) {
        // Animate the indicators on load
        const indicators = document.querySelectorAll('.indicator');
        indicators.forEach((indicator, index) => {
            setTimeout(() => {
                indicator.style.opacity = 1;
                indicator.style.transform = 'translateY(0)';
            }, 300 * index);
        });
    }
});