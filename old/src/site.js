const BG = 'assets/volshibkgd.png';
const SWIRL = 'assets/volshiswirlbkgd.png';
const STAR = 'assets/volshistarbkgd.png';
const TECH = 'assets/volshitechbkgd.png';
const WL = 'assets/volshilogowhite.png';
const ML = 'assets/volshimainlogo.png';

document.getElementById('wlogo').src = WL;
document.getElementById('alogo').src = ML;
document.getElementById('cwm').src   = WL;
document.getElementById('imark').src = WL;

// Backgrounds — raw image, no full-frame overlay. Scrim handled by CSS .scrim elements.
[
  {id:'bg0',img:BG,   pos:'center center'},
  {id:'bg1',img:TECH, pos:'center center'},
  {id:'bg2',img:SWIRL,pos:'center center'},
  {id:'bg3',img:STAR, pos:'center center'},
  {id:'bg4',img:TECH, pos:'65% 28%'},
  {id:'bg5',img:SWIRL,pos:'60% 55%'},
].forEach(b=>{
  const el=document.getElementById(b.id);
  if(el){el.style.backgroundImage=`url('${b.img}')`;el.style.backgroundPosition=b.pos;}
});

// Slide engine
const slides=Array.from(document.querySelectorAll('.slide'));
const navAs=Array.from(document.querySelectorAll('nav a'));
const hdr=document.getElementById('hdr');
const HASHES=['home','technology','archetron','research','company','contact'];
let cur=0,locked=false;
navAs.forEach(a=>a.classList.remove('on'));
hdr.classList.remove('solid');
slides.forEach((s,i)=>{s.style.transform=i===0?'translateX(0)':'translateX(100%)';});
slides[0].classList.add('active');

function goTo(n,push=true){
  if(n===cur||locked||n<0||n>5)return;
  locked=true;
  const dir=n>cur?1:-1;
  slides[cur].classList.remove('active');
  slides[cur].style.transition='transform 750ms cubic-bezier(0.76,0,0.24,1)';
  slides[cur].style.transform=`translateX(${-100*dir}%)`;
  slides[n].style.transition='none';
  slides[n].style.transform=`translateX(${100*dir}%)`;
  requestAnimationFrame(()=>requestAnimationFrame(()=>{
    slides[n].style.transition='transform 750ms cubic-bezier(0.76,0,0.24,1)';
    slides[n].style.transform='translateX(0)';
    slides[n].classList.add('active');
  }));
  cur=n;
  navAs.forEach((a,i)=>a.classList.toggle('on',i===n-1));
  hdr.classList.toggle('solid',n>0);
  if(push)history.pushState({s:n},'',`#${HASHES[n]}`);
  setTimeout(()=>locked=false,900);
}

navAs.forEach((a,i)=>a.addEventListener('click',e=>{e.preventDefault();goTo(i+1);}));
document.querySelector('.logo').addEventListener('click',()=>goTo(0));
document.querySelectorAll('[data-to]').forEach(el=>el.addEventListener('click',e=>{e.preventDefault();goTo(+el.dataset.to);}));
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')goTo(cur+1);if(e.key==='ArrowLeft')goTo(cur-1);});

let wAcc=0,wTimer;
document.addEventListener('wheel',e=>{
  e.preventDefault();
  wAcc+=Math.abs(e.deltaY||e.deltaX);
  clearTimeout(wTimer);wTimer=setTimeout(()=>wAcc=0,180);
  if(wAcc>80){wAcc=0;(e.deltaY>0||e.deltaX>0)?goTo(cur+1):goTo(cur-1);}
},{passive:false});

let tx=0,ty=0;
document.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
document.addEventListener('touchend',e=>{
  const dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>Math.abs(dy)&&Math.abs(dx)>50){dx<0?goTo(cur+1):goTo(cur-1);}
},{passive:true});

window.addEventListener('popstate',e=>{if(e.state?.s!=null)goTo(e.state.s,false);});
(()=>{
  const h=location.hash.replace('#',''),i=HASHES.indexOf(h);
  if(i>0){
    slides[0].style.transform='translateX(-100%)';slides[0].classList.remove('active');
    slides[i].style.transform='translateX(0)';slides[i].classList.add('active');
    cur=i;hdr.classList.add('solid');if(navAs[i-1])navAs[i-1].classList.add('on');
  }
})();

document.getElementById('mbtn').addEventListener('click',()=>document.getElementById('nav').classList.toggle('open'));
navAs.forEach(a=>a.addEventListener('click',()=>document.getElementById('nav').classList.remove('open')));
