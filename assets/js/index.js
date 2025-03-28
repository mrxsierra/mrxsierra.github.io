document.addEventListener('DOMContentLoaded', function() {

    // Typewriter effect function
    function typeWriter(text, targetId, speed) {
        let index = 0;
        const target = document.getElementById(targetId);

        function type() {
        if (index < text.length) {
            target.innerHTML += text.charAt(index);
            index++;
            setTimeout(type, speed);
        }
        }

        target.innerHTML = '';
        type();
    }

    // apply effect on page load
    // # welcome, name and explore ids are used in index.md
    typeWriter("✨🤚 Hey there Hello..! and Welcome to my Portfolio 🙏✨", 'welcome', 10);
    typeWriter("Sunil Sharma", 'name', 100);
    typeWriter("✨🤩 I'm thrilled to have you here. Explore my projects, read my blogs, and get to know more about me. ✨🤖", 'explore', 10);
});