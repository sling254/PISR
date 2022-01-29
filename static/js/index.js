// landing page js
const primaryNav = document.querySelector('#primary-navigation');
const navToggle = document.querySelector('.mobile-nav-toggle');


navToggle.addEventListener('click', ()=> {
    const visibility = primaryNav.getAttribute('data-visible')

    if (visibility === 'false'){
        primaryNav.setAttribute('data-visible', true)
        navToggle.setAttribute('aria-expanded', true)
    } else if(visibility === 'true'){
        primaryNav.setAttribute('data-visible', false)
        navToggle.setAttribute('aria-expanded', false)

    }
})


// landingpage animations
let tl = gsap.timeline({Defaults: {Easing: Expo.EaseIn}});

tl.to('.reveal', { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', y:0, stagger: .3, duration: 1})