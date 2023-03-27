
localStorage.setItem('mode', 'dark');
const mode = localStorage.getItem('mode');
console.log(mode === 'dark');

if(mode === 'dark'){
    // document.body.style.background = '#f0f2f5';
    document.body.style.background = '#fff';
}