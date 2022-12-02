(function(){
    
    const sliders = [...document.querySelectorAll('.goodslider__body')];
    console.log(sliders)
    const buttonNext = document.querySelector('#next');
    const buttonBefore = document.querySelector('#before');
    let value;   

    buttonNext.addEventListener('click', ()=>{
        changePosition(1);
    });

    buttonBefore.addEventListener('click', ()=>{
        changePosition(-1);
    });

    const changePosition = (add)=>{
        const currentgoodslider = document.querySelector('.goodslider__body--show').dataset.id;
        value = Number(currentgoodslider);
        value+= add;


        sliders[Number(currentgoodslider)-1].classList.remove('goodslider__body--show');
        if(value === sliders.length+1 || value === 0){
            value = value === 0 ? sliders.length  : 1;
        }

        sliders[value-1].classList.add('goodslider__body--show');

    }

})();