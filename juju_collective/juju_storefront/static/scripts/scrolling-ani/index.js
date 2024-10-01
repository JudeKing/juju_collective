document.addEventListener('DOMContentLoaded', () => {
	const header = document.querySelector(".nav-container .header-navbar ")
    const navMenuIcon = document.querySelector(".nav-menu__icon")
    const navMenuCloseIcon = document.querySelector(".nav-menu__close-icon")
    const navMenu = document.querySelector('.nav-menu')

    document.addEventListener('scroll', e => {
        if (window.scrollY > 0) {
            header.classList.add('slide-up')
            navMenuIcon.classList.add('slide-left')
        } else {
            console.log("BACK TO THE TOP")
            header.classList.remove('slide-up')
            navMenuIcon.classList.remove('slide-left')
        }
    })

    navMenuIcon.addEventListener('click', e => {
        navMenu.classList.add('slide-left')
    })

    navMenuCloseIcon.addEventListener('click', e => {
        navMenu.classList.remove('slide-left')
    })

})