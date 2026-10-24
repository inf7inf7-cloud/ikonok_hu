

(function(){
var NAME={top:'Nyitólap'},L='top',Q=null,cur=-1,P=null,ready=false,want=null,playing=false,ORD=null,pos=0;
var $=function(i){return document.getElementById(i)};
// kepek finom beusztatasa
function fade(img){if(img.complete&&img.naturalWidth)img.classList.add('ok');else img.addEventListener('load',function(){img.classList.add('ok')},{once:true})}
document.querySelectorAll('.ic img').forEach(fade);
// nyitolap: alapbol a top 100; csoportok, beallitasok popup, zeneszamlista
var LS=function(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}},WS=function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
var BY={};ALL.forEach(function(s){BY[s[0]]=s});var RANK={};TOPI.forEach(function(id,i){RANK[id]=i+1});
var HOME=(LS('home',null)||TOPI.slice()).filter(function(id){return BY[id]}),GRP=LS('grp',[]);
// csoportból / dobozból szabad helyre húzott ikonok: az oldal alján, doboz nélkül, egyenként (Miske, 10-23 15:22); HOME része
var LOOSE=LS('loose',[]).filter(function(id){return BY[id]});
// a top 100 naponta valtozhat: ha mas, mint a mentett nyitolapnal, a top resz ujra a friss sorrendben all, a kezzel hozzaadott (nem top) ikonok a vegen maradnak
(function(){var ot=LS('homet',null);if(LS('home',null)&&JSON.stringify(ot)!==JSON.stringify(TOPI)){var ex=ot?HOME.filter(function(id){return ot.indexOf(id)<0&&!RANK[id]}):[];HOME=TOPI.filter(function(id){return BY[id]}).concat(ex);WS('home',HOME)}WS('homet',TOPI)})();
// Mostanában slágerek (utóbbi 365 nap dalai): mindig a legelső csoport, új listánál frissül (FRESH a buildből)
// Mostanában slágerek: az utóbbi 12 hónap legjobb 50 dala sikerindex szerint (Miske, 10-24 10:16)
(function(){if(typeof FRESH==='undefined'||!FRESH.length)return;var _c=new Date(Date.now()-365*864e5).toISOString().slice(0,10),ids=FRESH.filter(function(p){return p[1]>=_c&&BY[p[0]]}).map(function(p){return p[0]}).slice(0,50),v=ids.join(','),k=-1;
 GRP.forEach(function(g,i){if(g.f)k=i});var del=LS('frissdel','');
 if(k<0&&del===v)return;if(k>=0&&GRP[k].v===v)return;
 ids.forEach(function(id){if(HOME.indexOf(id)<0)HOME.push(id)});
 var inU={};GRP.forEach(function(g){if(!g.f)g.ids.forEach(function(id){inU[id]=1})});ids=ids.filter(function(id){return!inU[id]});LOOSE=LOOSE.filter(function(id){return ids.indexOf(id)<0});
 var g={n:'Mostanában slágerek',ids:ids.slice(),f:1,w:99,v:v};if(k>=0){if(GRP[k].n&&['Legfrissebb 20 sláger','Aktuális Top 20','Aktuális','Aktuális slágerek'].indexOf(GRP[k].n)<0)g.n=GRP[k].n;g.w=GRP[k].w||g.w;GRP.splice(k,1)}GRP.unshift(g);save()})();
var OPT=LS('opt',null)||{sz:'m',t:!LS('notxt',false),a:true,c:1};DATA={top:[]};
var esc=function(t){return String(t).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
function hue(s){var h=0;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))%360;return h}
function save(){WS('home',HOME);WS('grp',GRP);WS('loose',LOOSE)}
function clean(){var H={};HOME.forEach(function(id){H[id]=1});var seen={};
 GRP.forEach(function(g){g.ids=g.ids.filter(function(id){if(!H[id]||seen[id])return false;seen[id]=1;return true})});
 GRP=GRP.filter(function(g){if(g.ids.length===1&&!g.f&&LOOSE.indexOf(g.ids[0])<0)LOOSE.push(g.ids[0]);return g.ids.length>1})}
function applyOpt(){var b=document.body.classList;['sz-x3','sz-x2','sz-x1','sz-s','sz-m','sz-l'].forEach(function(c){b.remove(c)});b.add('sz-'+OPT.sz);b.toggle('not',!OPT.t);b.toggle('noa',!OPT.a);b.toggle('showy',!!OPT.y);
 [['sz',OPT.sz],['cols',String(OPT.c)]].forEach(function(p){$(p[0]).querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x.dataset.v===p[1])})});
 $('oT').checked=OPT.t;$('oA').checked=OPT.a;if($('oY'))$('oY').checked=!!OPT.y;
 // méret/felirat váltás után a dobozok azonnal igazodjanak
 requestAnimationFrame(function(){lay();fitAll()})}
function tile(id,l){l=typeof l==='string'?l:'top';var s=BY[id],i=DATA[l].length;DATA[l].push([s[3],s[2],s[4]||'',id]);var lab=esc(s[3]+' – '+s[2]);
 var img=ICON[id]?'<img src="ikon/'+id+'.webp" alt="" width="256" height="256" loading="'+(i<14?'eager':'lazy')+'" decoding="async" draggable="false">':'<span style="position:absolute;inset:0;display:grid;place-items:center;color:#fff;font:800 34px system-ui;background:linear-gradient(135deg,hsl('+hue(s[3])+' 55% 40%),hsl('+(hue(s[3])+50)%360+' 60% 20%))">'+esc(s[3].charAt(0))+'</span>';
 return '<li data-id="'+id+'"><a class="ic" href="https://www.youtube.com/results?search_query='+encodeURIComponent(s[2]+' '+s[3])+'" target="_blank" rel="noopener" data-i="'+i+'" title="'+lab+'" aria-label="'+lab+'" style="--c:#2a2a3a" draggable="false">'+img+(RANK[id]?'<span class="rk">'+RANK[id]+'</span>':'')+'</a>'+(l==='fav'?'<button type="button" class="fx" data-fx="'+id+'" title="Levétel a kedvencek közül" aria-label="Levétel a kedvencek közül">✕</button>':'')+'<span class="ict" aria-hidden="true">'+esc(s[3])+'</span><span class="ica" aria-hidden="true">'+esc(s[2])+'</span>'+(s[1]?'<span class="icy" aria-hidden="true">'+s[1]+'</span>':'')+'</li>'}
function nC(){return innerWidth<=640?Math.min(OPT.c,2):OPT.c}
function grid(){clean();
 // ujrarajzolaskor (huzas, csoportositas) a lejatszo a dalt koveti, nem a sorszamot: a jelzo es a kovetkezo dal a hely helyett az ikonnal megy (Miske, 10-23 16:03)
 var oldT=Q==='top'?(DATA.top||[]).map(function(d){return d[3]}):null;DATA.top=[];var G={};GRP.forEach(function(g){g.ids.forEach(function(id){G[id]=1})});
 var ctl=function(k,w){return'<button type="button" class="wb" data-wb="'+k+'" title="Szélesség: '+w+' hasáb (kattints a váltáshoz)" aria-label="Szélesség váltása">'+'<i></i>'.repeat(w)+'</button>'};
 var box=function(k){var g=GRP[k];return'<section class="bx g" data-g="'+k+'"><span class="hd" aria-hidden="true"></span><div class="bxh" title="Húzd a fejlécnél fogva az áthelyezéshez"><input value="'+esc(g.n)+'" data-gn="'+k+'" aria-label="A csoport neve" maxlength="40">'+ctl(k,Math.min(g.w||1,nC()))+'<button type="button" class="x" data-ug="'+k+'" title="Csoport feloldása" aria-label="Csoport feloldása">✕</button></div><ol class="grid" data-list="top">'+g.ids.map(tile).join('')+'</ol><span class="rz" title="Húzd a szélesség állításához" aria-hidden="true"></span></section>'};
 LOOSE=LOOSE.filter(function(id){return!G[id]&&HOME.indexOf(id)>=0});var L0={};LOOSE.forEach(function(id){L0[id]=1});
 var rest=HOME.filter(function(id){return!G[id]&&!L0[id]}),mw=Math.min(OPT.mw||99,nC());
 $('main').innerHTML='<div id="bxs" class="boxes">'+GRP.map(function(g,k){return box(k)}).join('')+'<section class="bx main'+(GRP.length?'':' solo')+'" data-g="-1">'+(GRP.length&&rest.length?'<div class="bxh"><span>Mindenkori Top 100</span>'+ctl(-1,mw)+'</div>':'')+'<ol class="grid" id="g-top" data-list="top" aria-label="Nyitólap">'+rest.map(tile).join('')+'</ol>'+(GRP.length?'<span class="rz" title="Húzd a szélesség állításához" aria-hidden="true"></span>':'')+'</section></div>'+(LOOSE.length?'<ol class="grid" id="g-loose" data-list="top" aria-label="Egyéb ikonok">'+LOOSE.map(tile).join('')+'</ol>':'');
 document.querySelectorAll('.ic img').forEach(fade);applyOpt();lay();setTimeout(fitAll,0);
 if(oldT){var ni={};DATA.top.forEach(function(d,i){ni[d[3]]=i});var rm=function(i){var x=ni[oldT[i]];return x==null?-1:x};
  if(cur>=0)cur=rm(cur);if(ORD){ORD=ORD.map(rm).filter(function(x){return x>=0});var pp=ORD.indexOf(cur);if(pp>=0)pos=pp}}
}
// dobozok elrendezese: hasabracs, minden doboz 1..N hasab szeles, egymas alatt hezag nelkul
function spanOf(s){var k=+s.dataset.g,n=nC();return Math.max(1,Math.min(k<0?(OPT.mw||99):(GRP[k].w||1),n))}
function lay(){var c=$('bxs');if(!c)return;var n=nC(),W=c.clientWidth,gp=innerWidth<=640?14:22,cw=(W-(n-1)*gp)/n,H=[];for(var i=0;i<n;i++)H.push(0);
 // egyseges ikonmeret: az egyhasabos doboz sorat pontosan kitolti, minden mas doboz ugyanezt a meretet hasznalja
 var ic=parseFloat(getComputedStyle(document.body).getPropertyValue('--ic'))||121,g0=c.querySelector('.bx.g')||c.querySelector('.bx'),cs0=getComputedStyle(g0),pd=parseFloat(cs0.paddingLeft)+parseFloat(cs0.paddingRight),gc=parseFloat(getComputedStyle(g0.querySelector('.grid')).columnGap)||14,
  in1=(GRP.length?cw:W)-pd,k=Math.max(1,Math.round((in1+gc)/(ic+gc))),S=Math.floor(((in1+gc)/k-gc)*10)/10;c.style.setProperty('--S',S+'px');
 [].forEach.call(c.children,function(s){var w=spanOf(s);s.style.width=(cw*w+gp*(w-1))+'px';var h=s.offsetHeight,best=0,bt=1e9;
  for(var st=0;st+w<=n;st++){var t=Math.max.apply(null,H.slice(st,st+w));if(t<bt-1){bt=t;best=st}}
  s.style.left=best*(cw+gp)+'px';s.style.top=bt+'px';for(var q=best;q<best+w;q++)H[q]=bt+h+gp});
 c.style.height=Math.max(0,Math.max.apply(null,H)-gp)+'px';if(!c._a){c._a=1;requestAnimationFrame(function(){c.classList.add('an')})}}
function setSpan(k,w){if(k<0)OPT.mw=w,WS('opt',OPT);else GRP[k].w=w,save();var s=document.querySelector('#bxs .bx[data-g="'+k+'"]'),b=s&&s.querySelector('.wb');if(b){b.innerHTML='<i></i>'.repeat(w);b.title='Szélesség: '+w+' hasáb (kattints a váltáshoz)'}lay()}
grid();
// csoportnev, feloldas
$('main').addEventListener('change',function(e){var k=e.target.dataset.gn;if(k==null)return;GRP[k].n=e.target.value.trim()||'Csoport';save()});
$('main').addEventListener('keydown',function(e){if(e.target.dataset.gn!=null&&e.key==='Enter')e.target.blur()});
$('main').addEventListener('click',function(e){var y=e.target.closest('[data-ugy]');if(y){if(GRP[+y.dataset.ugy].f)WS('frissdel',GRP[+y.dataset.ugy].ids.join(','));GRP[+y.dataset.ugy].ids.forEach(function(id){if(LOOSE.indexOf(id)<0)LOOSE.push(id)});GRP.splice(+y.dataset.ugy,1);save();grid();mark();return}
 if(e.target.closest('.ugn')){e.target.closest('.ugq').remove();return}
 var k=e.target.dataset.ug;if(k==null)return;var bx=e.target.closest('.bx');if(bx.querySelector('.ugq'))return;
 var q=document.createElement('div');q.className='ugq';q.setAttribute('role','alertdialog');q.innerHTML='<p>Biztosan törlöd a „'+esc(GRP[k].n)+'” csoportot?</p><small>Az ikonok nem vesznek el, az oldal aljára kerülnek.</small><div><button type="button" class="pri" data-ugy="'+k+'">Igen, törlöm</button><button type="button" class="sec ugn">Mégse</button></div>';bx.appendChild(q);q.querySelector('.ugn').focus()});
// huzas: telefonon lenyomva tartas, egerrel lenyomva huzas
var D=null,noClick=false;
// célpont húzáskor (Miske, 10-23 18:56): az ikon közepére dobva csoport, az ikon szélére vagy két ikon közé (a résbe) dobva beszúrás oda
function pickT(x,y,sc,me){var el=document.elementFromPoint(x,y);if(!el)return null;var li=el.closest(sc+' li[data-id]');
 if(li&&+li.dataset.id!==me){var ic=li.querySelector('.ic'),r=(ic||li).getBoundingClientRect(),f=(x-r.left)/r.width;
  if(el.closest('.ic'))return{li:li,mode:f<.28?'b':f>.72?'a':'on'};return{li:li,mode:f<.5?'b':'a'}}
 var gr=el.closest(sc+' .grid');if(gr){var best=null,bd=1e9;[].forEach.call(gr.children,function(q){if(!q.dataset||!q.dataset.id||+q.dataset.id===me)return;var r=q.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2,d=Math.abs(cx-x)+2*Math.abs(cy-y);if(d<bd){bd=d;best={li:q,mode:x<cx?'b':'a'}}});if(best)return best}
 return null}
function insMark(t){document.querySelectorAll('.insb,.insa').forEach(function(q){q.classList.remove('insb','insa')});var on=!!(t&&t.li&&t.mode!=='on');document.body.classList.toggle('insmode',on);if(on)t.li.classList.add(t.mode==='b'?'insb':'insa')}
function tgtAt(x,y){var t=pickT(x,y,'#main',D.id);if(t)return t;var el=document.elementFromPoint(x,y),bx=el&&el.closest('#main .bx');return bx?{bx:bx}:null}
function hl(t){document.querySelectorAll('#main .tgt').forEach(function(x){x.classList.remove('tgt')});insMark(t);if(!t)return;if(t.li){if(t.mode==='on')t.li.querySelector('.ic').classList.add('tgt')}else t.bx.classList.add('tgt')}
function startDrag(){var a=D.li.querySelector('.ic'),r=a.getBoundingClientRect(),g=document.createElement('div');g.id='ghost';g.style.setProperty('--gw',r.width+'px');
 var im=a.querySelector('img');g.innerHTML=im?'<img src="'+im.src+'" alt="">':'';if(!im)g.style.background='#456';document.body.appendChild(g);
 D.g=g;D.on=true;D.li.classList.add('drag');document.body.classList.add('dragging');move(D.x,D.y);if(navigator.vibrate)try{navigator.vibrate(15)}catch(e){}}
function move(x,y){D.x=x;D.y=y;if(!D.on)return;D.g.style.left=x+'px';D.g.style.top=y+'px';D.t=tgtAt(x,y);hl(D.t);
 var m=60;if(y<m)scrollBy(0,-12);else if(y>innerHeight-m)scrollBy(0,12)}
function where(id){for(var k=0;k<GRP.length;k++)if(GRP[k].ids.indexOf(id)>=0)return k;return -1}
function drop(){var t=D.t,id=D.id,from=where(id);
 // szabad helyre (dobozon kivulre) huzva: kikerul a dobozbol/csoportbol, az oldal aljara, doboz nelkul, egyenkent
 if(!t){if(from>=0)GRP[from].ids=GRP[from].ids.filter(function(x){return x!==id});LOOSE=LOOSE.filter(function(x){return x!==id});LOOSE.push(id);save();grid();mark();return}
 LOOSE=LOOSE.filter(function(x){return x!==id});
 // beszúrás a célikon elé/mögé, ugyanabba a dobozba / csoportba / listába
 if(t.li&&t.mode!=='on'){var to=+t.li.dataset.id,k=where(to),af=t.mode==='a'?1:0;if(from>=0)GRP[from].ids=GRP[from].ids.filter(function(x){return x!==id});
  if(k>=0)GRP[k].ids.splice(GRP[k].ids.indexOf(to)+af,0,id);
  else{if(LOOSE.indexOf(to)>=0)LOOSE.splice(LOOSE.indexOf(to)+af,0,id);HOME=HOME.filter(function(x){return x!==id});var hi=HOME.indexOf(to);HOME.splice(hi<0?HOME.length:hi+af,0,id)}
  save();grid();mark();return}
 if(t.li){var to=+t.li.dataset.id,k=where(to);if(from>=0)GRP[from].ids=GRP[from].ids.filter(function(x){return x!==id});
  // a Mostanában slágerek dobozban is ikonra huzva uj csoport keletkezik (Miske, 10-23)
  if(k>=0&&GRP[k].f){GRP[k].ids=GRP[k].ids.filter(function(x){return x!==to});k=-1}
  LOOSE=LOOSE.filter(function(x){return x!==to});
  if(k>=0){var at=GRP[k].ids.indexOf(to);GRP[k].ids.splice(at+1,0,id)}
  else{GRP.push({n:'Csoport '+(GRP.length+1),ids:[to,id],w:1});
   // az uj csoport a helyen marad: a nyitolap sorrendjeben az elso tag helyere kerul a masik
   HOME=HOME.filter(function(x){return x!==id});HOME.splice(HOME.indexOf(to)+1,0,id)}}
 else{var g=+t.bx.dataset.g;if(g===from)return;if(from>=0)GRP[from].ids=GRP[from].ids.filter(function(x){return x!==id});
  if(g>=0)GRP[g].ids.push(id);else{HOME=HOME.filter(function(x){return x!==id});HOME.push(id)}}
 save();grid();mark()}
function end(ok){if(!D)return;clearTimeout(D.tm);insMark(null);if(D.on){if(ok)drop();if(D.g)D.g.remove();D.li.classList.remove('drag');document.body.classList.remove('dragging');hl(null);noClick=true;setTimeout(function(){noClick=false},350)}D=null}
$('main').addEventListener('pointerdown',function(e){if(e.button>0)return;var li=e.target.closest('li[data-id]');if(!li||!e.target.closest('.ic'))return;
 D={li:li,id:+li.dataset.id,x:e.clientX,y:e.clientY,x0:e.clientX,y0:e.clientY,on:false,touch:e.pointerType!=='mouse'};
 D.tm=setTimeout(function(){if(D&&!D.on)startDrag()},D.touch?420:300)});
addEventListener('pointermove',function(e){if(!D)return;var dx=e.clientX-D.x0,dy=e.clientY-D.y0,far=dx*dx+dy*dy>64;
 if(!D.on){if(far){if(D.touch){clearTimeout(D.tm);D=null;return}startDrag()}else return}move(e.clientX,e.clientY)});
addEventListener('pointerup',function(){end(true)});addEventListener('pointercancel',function(){end(false)});
addEventListener('touchmove',function(e){if(D&&D.on)e.preventDefault()},{passive:false});
addEventListener('contextmenu',function(e){if(e.target.closest&&e.target.closest('#main .ic'))e.preventDefault()});
addEventListener('click',function(e){if(noClick){e.preventDefault();e.stopPropagation()}},true);
addEventListener('keydown',function(e){if(e.key==='Escape')end(false)});
// csoportdoboz athelyezese a fejlecnel fogva, szelesseg allitasa
var B=null;
$('main').addEventListener('click',function(e){var b=e.target.closest('[data-wb]');if(!b)return;var k=+b.dataset.wb,s=b.closest('.bx'),w=spanOf(s)%nC()+1;setSpan(k,w)});
$('main').addEventListener('pointerdown',function(e){if(e.button>0)return;var rz=e.target.closest('#bxs .rz');
 if(rz){e.preventDefault();var s=rz.parentNode;B={rz:true,s:s,k:+s.dataset.g,on:true,x0:e.clientX,y0:e.clientY};s.classList.add('rs');document.body.classList.add('dragging');return}
 var h=e.target.closest('.bx.g .bxh,.bx.g .hd');if(!h||e.target.closest('input:focus,.x,.wb'))return;
 B={s:h.closest('.bx'),x0:e.clientX,y0:e.clientY,on:false,touch:e.pointerType!=='mouse'};B.tm=setTimeout(function(){if(B&&!B.on)bStart()},B.touch?380:250)});
function bStart(){B.on=true;B.s.classList.add('mv');document.body.classList.add('dragging');var i=B.s.querySelector('input');if(i)i.blur();if(navigator.vibrate)try{navigator.vibrate(15)}catch(e){}}
function bMove(x,y){var c=$('bxs');
 if(B.rz){var n=nC(),gp=innerWidth<=640?14:22,cw=(c.clientWidth-(n-1)*gp)/n,r=B.s.getBoundingClientRect(),w=Math.max(1,Math.min(n,Math.round((x-r.left+gp)/(cw+gp))));if(w!==spanOf(B.s))setSpan(B.k,w);return}
 var o=null;[].some.call(c.querySelectorAll('.bx.g'),function(s){if(s===B.s)return false;var r=s.getBoundingClientRect();if(x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom){o={s:s,r:r};return true}});
 if(o){var after=y>o.r.top+o.r.height/2,ref=after?o.s.nextSibling:o.s;if(ref!==B.s&&B.s.nextSibling!==ref){c.insertBefore(B.s,ref);lay()}}
 var m=60;if(y<m)scrollBy(0,-12);else if(y>innerHeight-m)scrollBy(0,12)}
function bEnd(ok){if(!B)return;clearTimeout(B.tm);if(B.on){B.s.classList.remove('mv','rs');document.body.classList.remove('dragging');noClick=true;setTimeout(function(){noClick=false},350);
  if(!B.rz){var NG=[];document.querySelectorAll('#bxs .bx.g').forEach(function(s){NG.push(GRP[+s.dataset.g])});GRP=NG;save();grid();mark()}}B=null}
addEventListener('pointermove',function(e){if(!B)return;var dx=e.clientX-B.x0,dy=e.clientY-B.y0;if(!B.on){if(dx*dx+dy*dy>64){if(B.touch){clearTimeout(B.tm);B=null;return}bStart()}else return}bMove(e.clientX,e.clientY)});
addEventListener('pointerup',function(){bEnd(true)});addEventListener('pointercancel',function(){bEnd(false)});
addEventListener('touchmove',function(e){if(B&&B.on)e.preventDefault()},{passive:false});
var rw=innerWidth<=640,rl,lw=innerWidth;addEventListener('resize',function(){if(innerWidth===lw)return;lw=innerWidth;var m=innerWidth<=640;if(m!==rw){rw=m;grid();mark();return}clearTimeout(rl);rl=setTimeout(lay,60)});
// beallitasok popup
var dlg=$('dlg');
$('bset').onclick=function(){applyOpt();$('resetQ').hidden=true;dlg.showModal()};
dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
$('sz').onclick=function(e){var v=e.target.dataset.v;if(!v)return;OPT.sz=v;WS('opt',OPT);applyOpt()};
$('cols').onclick=function(e){var v=e.target.dataset.v;if(!v)return;OPT.c=+v;WS('opt',OPT);grid();mark();if(!$('fav').hidden)renderFav()};
// ikonmeret, felirat: egy kozos beallitas a nyitolapon es a Kedvenceimben is, mindket elrendezes azonnal ujraszamol (Miske, 10-23 16:30)
// doboz nelkuli racsok (Kedvenceim szabad ikonjai, nyitolap alja): ugyanugy kitoltik a sort, mint a dobozok, igy minden oldalon azonos az ikonmeret
function fitS(el){if(!el||!el.clientWidth)return;var ic=parseFloat(getComputedStyle(document.body).getPropertyValue('--ic'))||121,gc=parseFloat(getComputedStyle(el).columnGap)||14,W=el.clientWidth,k=Math.max(1,Math.round((W+gc)/(ic+gc)));el.style.setProperty('--S',Math.floor(((W+gc)/k-gc)*10)/10+'px')}
function fitAll(){fitS($('g-fav'));fitS($('g-loose'))}addEventListener('resize',fitAll);
var relay=function(){lay();if(typeof flay==='function')flay();fitAll()};$('sz').addEventListener('click',function(){setTimeout(relay,0)});$('oT').addEventListener('change',relay);$('oA').addEventListener('change',relay);
$('oT').onchange=function(){OPT.t=this.checked;WS('opt',OPT);applyOpt()};$('oA').onchange=function(){OPT.a=this.checked;WS('opt',OPT);applyOpt()};$('oY').onchange=function(){OPT.y=this.checked;WS('opt',OPT);applyOpt();try{lay();fitAll()}catch(e){}};
$('reset').onclick=function(){$('resetQ').hidden=false};
$('resetY').onclick=function(){go('top');HOME=TOPI.slice();GRP=[];LOOSE=[];OPT={sz:'m',t:true,a:true,c:1};ORDL='idx';AF=null;['home','grp','loose','opt','ord','theme','notxt'].forEach(function(k){try{localStorage.removeItem(k)}catch(e){}});delete document.documentElement.dataset.theme;grid();mark();dlg.close();scrollTo(0,0)};
// ha lejatszas kozben valtozik a lista (szures, kereses, levetel), a regi lista befagy: a dal vegen leall, nem ugrik idegen szamra
function freeze(l){if(Q===l){DATA[l+'0']=DATA[l];NAME[l+'0']=NAME[l];Q=l+'0'}}
function thaw(l){var o=DATA[l+'0'];if(Q===l+'0'&&o&&o.map(function(x){return x[3]}).join()===DATA[l].map(function(x){return x[3]}).join())Q=l}
// zeneszamlista
var norm=function(s){return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')};
var AF=null,ORDL=LS('ord','idx')==='top'?'rank':LS('ord','idx'),ART=[];(function(){var c={};ALL.forEach(function(s){c[s[2]]=(c[s[2]]||0)+1});ART=Object.keys(c).sort(function(a,b){return a.localeCompare(b,'hu')}).map(function(a){return[a,c[a]]})})();
function nCol(){return innerWidth>900?6:innerWidth>560?3:2}
function renderArts(){var qq=AF?'':norm($('q').value.trim()),AR=qq?ART.filter(function(a){return norm(a[0]).indexOf(qq)>=0}):ART,n=Math.max(1,Math.min(nCol(),AR.length)),per=Math.ceil(AR.length/n),q=$('q').value,h='';
 for(var c=0;c<n;c++)h+='<div>'+AR.slice(c*per,(c+1)*per).map(function(a){return'<button type="button" data-ar="'+esc(a[0])+'" class="'+(AF===a[0]?'on':'')+'" title="'+esc(a[0])+'">'+esc(a[0])+' <small>'+a[1]+'</small></button>'}).join('')+'</div>';
 $('arts').style.gridTemplateColumns='repeat('+nCol()+',minmax(0,1fr))';$('arts').innerHTML=h;$('arts').hidden=!AR.length}
function markArts(){$('arts').querySelectorAll('.on').forEach(function(b){b.classList.remove('on')});if(AF){var b=$('arts').querySelector('[data-ar="'+AF.replace(/"/g,'\\"')+'"]');if(b)b.classList.add('on')}}
var YO=null,YS=function(a,b){return(a==='0')-(b==='0')||(a<b?-1:a>b?1:0)};
function renderList(){var q=norm($('q').value),H={};FAV.forEach(function(id){H[id]=1});var by={},n=0;
 // Év/sikerindex, Év/ABC: évenkénti dobozok; Sikerindex, ABC: egy folyamatos lista 3 hosszú hasábban (telefonon 1), évek nélkül (Miske, 10-23 15:41)
 var TL=ORDL==='rank',LG=TL||ORDL==='nabc',RR={};RLI.forEach(function(id,i){RR[id]=i+1});
 ALL.forEach(function(s){if(AF?s[2]!==AF:(q&&norm(s[2]+' '+s[3]).indexOf(q)<0))return;n++;var k=LG?'L':s[1];(by[k]=by[k]||[]).push(s)});
 var LBL={};
 // Sikerindex: 100-as blokkok (1–100, 101–200, …) (Miske, 10-23 17:14)
 if(TL&&by.L){var bl={};by.L.forEach(function(s){var r=RR[s[0]]||1e9,b=r<1e9?Math.floor((r-1)/100):999;(bl[b]=bl[b]||[]).push(s)});by={};
  Object.keys(bl).forEach(function(b){var k='c'+('00'+b).slice(-3);by[k]=bl[b].sort(function(x,y){return(RR[x[0]]||1e9)-(RR[y[0]]||1e9)});LBL[k]=b==999?'Rangsoron kívül':(b*100+1)+'–'+(b*100+100)})}
 else if(LG&&by.L){var arr=by.L.sort(TL?function(a,b){return(RR[a[0]]||1e9)-(RR[b[0]]||1e9)}:function(a,b){return a[2].localeCompare(b[2],'hu')||a[3].localeCompare(b[3],'hu')}),nl=Math.min(arr.length,innerWidth>900?3:innerWidth>560?2:1),per=Math.ceil(arr.length/nl);by={};
  for(var c=0;c<nl;c++){var ch=arr.slice(c*per,(c+1)*per);if(!ch.length)continue;by['c'+c]=ch;var f=ch[0],l=ch[ch.length-1];LBL['c'+c]=TL?(RR[f[0]]||'')+'–'+(RR[l[0]]||''):f[2].charAt(0).toUpperCase()+(f[2].charAt(0).toUpperCase()!==l[2].charAt(0).toUpperCase()?'–'+l[2].charAt(0).toUpperCase():'')}}
 var cmp=LG?function(){return 0}:ORDL==='abc'?function(a,b){return a[2].localeCompare(b[2],'hu')||a[3].localeCompare(b[3],'hu')}:function(a,b){return b[5]-a[5]||a[3].localeCompare(b[3],'hu')};
 freeze('lst');DATA.lst=[];NAME.lst='Zeneszámlista';var YH=Object.keys(by).sort(YS).map(function(yr){var yl=LG?LBL[yr]:yr==='0'?'Évszám nélkül':yr,af=by[yr].every(function(s){return H[s[0]]});return'<div class="yb" data-yl="'+yl+'"><h3>'+yl+'<span class="ya"><button type="button" class="yf'+(af?' on':'')+'" data-yb="f" title="'+(af?'A doboz számainak levétele a kedvencek közül':'A doboz összes számát a Kedvenceimhez')+'" aria-label="A doboz összes száma a kedvencekhez">'+(af?'★':'☆')+'</button><button type="button" data-yb="p" title="A doboz lejátszása sorban" aria-label="A doboz lejátszása sorban"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2v12l10-6z" fill="currentColor"/></svg><span class="pl">Lejátszás</span></button><button type="button" data-yb="s" title="A doboz lejátszása keverve" aria-label="A doboz lejátszása keverve"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h3.5c2 0 3.2.9 4.3 2.6l2.4 4.8c1.1 1.7 2.3 2.6 4.3 2.6H21M3 17h3.5c2 0 3.2-.9 4.3-2.6M13.2 9.6c1.1-1.7 2.3-2.6 4.3-2.6H21M18 4l3 3-3 3M18 14l3 3-3 3"/></svg><span class="pl">Kevert lejátszás</span></button></span><small>'+by[yr].length+'</small></h3>'+by[yr].sort(cmp).map(function(s){return(DATA.lst.push([s[3],s[2],s[4]||'',s[0]]),'')+'<div class="sr2"><a class="pb" data-p="'+(DATA.lst.length-1)+'" href="https://www.youtube.com/results?search_query='+encodeURIComponent(s[2]+' '+s[3])+'" target="_blank" rel="noopener" title="Lejátszás" aria-label="'+esc(s[3])+' lejátszása"></a><span class="tx">'+(TL&&RR[s[0]]?'<i class="rn">'+RR[s[0]]+'.</i> ':'')+'<button type="button" class="arl" data-ar="'+esc(s[2])+'" title="'+esc(s[2])+' összes száma">'+esc(s[2])+'</button> – <a data-p="'+(DATA.lst.length-1)+'" href="https://www.youtube.com/results?search_query='+encodeURIComponent(s[2]+' '+s[3])+'" target="_blank" rel="noopener" title="Lejátszás"><b>'+esc(s[3])+'</b></a>'+(LG&&s[1]?' <i class="ye">'+s[1]+'</i>':'')+'</span><button type="button" class="st'+(H[s[0]]?' on':'')+'" data-a="'+s[0]+'" aria-label="'+(H[s[0]]?'Levétel a kedvencek közül':'Kedvenceimhez')+'" title="'+(H[s[0]]?'Levétel a kedvencek közül':'Kedvenceimhez')+'">'+(H[s[0]]?'★':'☆')+'</button></div>'}).join('')+'</div>'}),YN=(thaw('lst'),Object.keys(by).sort(YS).map(function(y){return by[y].length+3})),ye=$('years'),nc=YH.length?(innerWidth>900?3:innerWidth>560?2:1):0,hh=[],k=0;
 if(YO)YO.disconnect();ye.innerHTML=nc?new Array(nc+1).join('<div class="yc"></div>'):'<p class="hint">Nincs találat.</p>';for(var c=0;c<nc;c++)hh.push(0);
 // fokozatos kirajzolás: hasábonként a legrövidebbhez, a többi évet csak görgetéskor teszi be (a több ezer sor egyszerre akasztott)
 function add(m){var e=Math.min(YH.length,k+m),cs=ye.children;for(;k<e;k++){var j=hh.indexOf(Math.min.apply(null,hh));cs[j].insertAdjacentHTML('beforeend',YH[k]);hh[j]+=YN[k]}}
 var s0=0;if(LG)add(YH.length);while(k<YH.length&&s0<260*nc){s0+=YN[k];add(1)}
 if(k<YH.length&&'IntersectionObserver' in window){YO=new IntersectionObserver(function(en){if(en[0].isIntersecting){add(6*nc);if(k>=YH.length)YO.disconnect()}},{rootMargin:'1200px 0px'});YO.observe($('ysent'))}else add(YH.length);
 $('ord').querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x.dataset.v===ORDL)});
 var fb=$('afbar');fb.hidden=!AF;if(AF){var aids=ALL.filter(function(s){return s[2]===AF}).map(function(s){return s[0]}),aon=aids.length&&aids.every(function(id){return H[id]});
  fb.innerHTML='<span class="afl">Csak <b>'+esc(AF)+'</b> számai ('+n+')</span><span class="ya afa"><button type="button" class="yf'+(aon?' on':'')+'" data-af="f" title="'+(aon?'Az előadó számainak levétele a kedvencek közül':'Az előadó összes száma egy dobozban a Kedvenceimhez')+'" aria-label="Az előadó a kedvencekhez">'+(aon?'★':'☆')+'</button><button type="button" data-af="p" title="Az előadó számainak lejátszása sorban" aria-label="Lejátszás sorban"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2v12l10-6z" fill="currentColor"/></svg><span class="pl">Lejátszás</span></button><button type="button" data-af="s" title="Az előadó számainak lejátszása keverve" aria-label="Lejátszás keverve"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h3.5c2 0 3.2.9 4.3 2.6l2.4 4.8c1.1 1.7 2.3 2.6 4.3 2.6H21M3 17h3.5c2 0 3.2-.9 4.3-2.6M13.2 9.6c1.1-1.7 2.3-2.6 4.3-2.6H21M18 4l3 3-3 3M18 14l3 3-3 3"/></svg><span class="pl">Kevert lejátszás</span></button></span><button type="button" class="pri" id="afx">↩ Vissza az éves dobozokhoz</button>'}}
$('afbar').onclick=function(e){var b=e.target.closest('[data-af]');
 if(b){var v=b.dataset.af;
  // elooado: a csillag egy elooadoi dobozba teszi a kedvencek koze (ujra nyomva leveszi), a ket gomb sorban / keverve jatssza
  if(v==='f'){var ids=ALL.filter(function(s){return s[2]===AF}).map(function(s){return s[0]}),all=ids.every(function(id){return FAV.indexOf(id)>=0});
   FAV=all?FAV.filter(function(id){return ids.indexOf(id)<0}):FAV.concat(ids.filter(function(id){return FAV.indexOf(id)<0}));
   if(!all){FAVG.forEach(function(g){g.ids=g.ids.filter(function(id){return ids.indexOf(id)<0})});FAVG=FAVG.filter(function(g){return g.n!==AF});FAVG.push({n:AF,ids:ids.slice()})}
   favSave();favN();renderList();return}
  if(!DATA.lst.length)return;if(!ready){var a0=document.querySelector('#years .pb');if(a0)window.open(a0.href,'_blank');return}
  document.querySelectorAll('.sr2.on').forEach(function(x){x.classList.remove('on')});if(v==='s')shuffle('lst');else{ORD=null;play('lst',0)}return}
 if(!e.target.closest('#afx'))return;AF=null;$('q').value='';renderList();markArts()};
$('nAll').textContent=ALL.length.toLocaleString('hu-HU');
// evdoboz gombjai: mind a kedvencekhez (ujra nyomva le), lejatszas sorban, keverve
function yBox(b){var box=b.closest('.yb'),v=b.dataset.yb;
 if(v==='f'){var ids=[].map.call(box.querySelectorAll('.st[data-a]'),function(x){return +x.dataset.a}),all=ids.every(function(id){return FAV.indexOf(id)>=0});
  FAV=all?FAV.filter(function(id){return ids.indexOf(id)<0}):FAV.concat(ids.filter(function(id){return FAV.indexOf(id)<0}));
  if(!all){var nm=box.dataset.yl+(AF?' · '+AF:''),q=$('q').value.trim();if(!AF&&q)nm+=' · „'+q+'”';FAVG.forEach(function(g){g.ids=g.ids.filter(function(id){return ids.indexOf(id)<0})});FAVG=FAVG.filter(function(g){return g.n!==nm});FAVG.push({n:nm,ids:ids.slice()})}
  favSave();favN();
  box.querySelectorAll('.st[data-a]').forEach(function(x){x.classList.toggle('on',!all);x.textContent=all?'☆':'★';x.title=all?'Kedvenceimhez':'Levétel a kedvencek közül';x.setAttribute('aria-label',x.title)});
  b.classList.toggle('on',!all);b.textContent=all?'☆':'★';b.title=all?'A doboz összes számát a Kedvenceimhez':'A doboz számainak levétele a kedvencek közül';return}
 DATA.yr=[].map.call(box.querySelectorAll('.sr2 .pb[data-p]'),function(a){return DATA.lst[+a.dataset.p]});NAME.yr=box.dataset.yl;if(!DATA.yr.length)return;
 if(!ready){window.open(box.querySelector('.pb').href,'_blank');return}
 document.querySelectorAll('.sr2.on').forEach(function(x){x.classList.remove('on')});if(v==='s')shuffle('yr');else{ORD=null;play('yr',0)}}
// fulek: nyitolap, kedvenceim, valogato
var FAV=LS('fav',[]).filter(function(id){return BY[id]}),FAVG=LS('favg',[]);NAME.fav='Kedvenceim';DATA.fav=[];
// FAVG: a Valogatobol egeszben felvett dobozok ({n,ids}); a tobbi kedvenc szabadon, a FAV sorrendjeben
function favSave(){var F={};FAV.forEach(function(id){F[id]=1});var s={};FAVG.forEach(function(g){g.ids=g.ids.filter(function(id){if(!F[id]||s[id])return false;s[id]=1;return true})});FAVG=FAVG.filter(function(g){return g.ids.length});WS('fav',FAV);WS('favg',FAVG)}
function favG(id){for(var k=0;k<FAVG.length;k++)if(FAVG[k].ids.indexOf(id)>=0)return k;return -1}
function favN(){$('nFav').textContent=FAV.length?' ('+FAV.length+')':''}
function renderFav(){favSave();freeze('fav');DATA.fav=[];var G={};FAVG.forEach(function(g){g.ids.forEach(function(id){G[id]=1})});
 var fw=function(k){return Math.max(1,Math.min(FAVG[k].w||99,nC()))};
 $('favB').innerHTML=FAVG.length?'<div id="fbxs" class="boxes">'+FAVG.map(function(g,k){var w=fw(k);return'<section class="bx g" data-fg="'+k+'"><span class="hd" aria-hidden="true"></span><div class="bxh" title="Húzd a fejlécnél fogva az áthelyezéshez"><input value="'+esc(g.n)+'" data-fgn="'+k+'" aria-label="A doboz neve" maxlength="60"><small class="fbn">'+g.ids.length+'</small><button type="button" class="wb" data-fwb="'+k+'" title="Szélesség: '+w+' hasáb (kattints a váltáshoz)" aria-label="Szélesség váltása">'+'<i></i>'.repeat(w)+'</button><button type="button" class="x fgx" data-fgx="'+k+'" title="A doboz levétele a kedvencek közül" aria-label="A doboz levétele a kedvencek közül">✕</button></div><ol class="grid" data-list="fav">'+g.ids.map(function(id){return tile(id,'fav')}).join('')+'</ol><span class="rz" title="Húzd a szélesség állításához" aria-hidden="true"></span></section>'}).join('')+'</div>':'';
 var L0=FAV.filter(function(id){return!G[id]});$('g-fav').innerHTML=L0.map(function(id){return tile(id,'fav')}).join('');setTimeout(fitAll,0);$('favLH').hidden=!(FAVG.length&&L0.length);thaw('fav');$('favE').hidden=!!FAV.length;$('favT').hidden=!FAV.length;document.querySelectorAll('#fav .ic img').forEach(fade);mark();flay()}
function go(v){dlg.close();L=v==='fav'?'fav':'top';$('main').hidden=v!=='top';$('fav').hidden=v!=='fav';$('lista').hidden=v!=='lista';
 $('tabs').querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===v)});
 if(v==='top'){grid();mark()}else if(v==='fav')renderFav();else{renderArts();renderList()}scrollTo(0,0)}
$('tabs').onclick=function(e){var b=e.target.closest('[data-t]');if(b)go(b.dataset.t)};
// kedvenc levétele után 8 mp-ig „Visszavonás” (Miske, 10-23: ne lehessen egy mellényomással törölni)
function favUndo(msg){var F0=FAV.slice(),G0=JSON.parse(JSON.stringify(FAVG)),o=$('fundo');if(o)o.remove();
 var t=document.createElement('div');t.id='fundo';t.setAttribute('role','status');t.innerHTML='<span>'+msg.replace(/</g,'&lt;')+'</span><button type="button">Visszavonás</button>';
 var d=$('dock');t.style.bottom=((d&&!d.hidden?d.offsetHeight:0)+14)+'px';document.body.appendChild(t);
 var tm=setTimeout(function(){t.remove()},8000);
 return function(){t.querySelector('button').onclick=function(){clearTimeout(tm);t.remove();FAV=F0;FAVG=G0;favSave();favN();renderFav();if(typeof favBtn==='function')favBtn()}}}
$('fav').addEventListener('click',function(e){var x=e.target.closest('[data-fgx]');if(x){e.preventDefault();e.stopPropagation();
  // ketlepcsos: elso kattintasra rakerdez
  if(!x.classList.contains('sure')){x.classList.add('sure');x.textContent='Biztosan leveszed?';setTimeout(function(){if(x.isConnected){x.classList.remove('sure');x.textContent='✕'}},4000);return}
  var g=FAVG[+x.dataset.fgx],u=favUndo('Doboz levéve');FAV=FAV.filter(function(id){return g.ids.indexOf(id)<0});favSave();favN();renderFav();u();return}
 var b=e.target.closest('[data-fx]');if(!b)return;e.preventDefault();e.stopPropagation();var id=+b.dataset.fx,u=favUndo('Levéve: '+BY[id][3]);FAV=FAV.filter(function(x){return x!==id});favSave();favN();renderFav();u()},true);
$('favGo').onclick=function(){go('lista')};favN();
// kedvenc dobozok: a nyitolapi dobozokhoz hasonloan atnevezheto, szelessege allithato, a fejlecnel fogva athelyezheto
function fSpan(s){var n=nC();return Math.max(1,Math.min(FAVG[+s.dataset.fg].w||99,n))}
function flay(){var c=$('fbxs');if(!c||$('fav').hidden)return;var n=nC(),W=c.clientWidth,gp=innerWidth<=640?14:22,cw=(W-(n-1)*gp)/n,H=[];for(var i=0;i<n;i++)H.push(0);
 var ic=parseFloat(getComputedStyle(document.body).getPropertyValue('--ic'))||121,g0=c.querySelector('.bx');if(!g0)return;var cs0=getComputedStyle(g0),pd=parseFloat(cs0.paddingLeft)+parseFloat(cs0.paddingRight),gc=parseFloat(getComputedStyle(g0.querySelector('.grid')).columnGap)||14,
  in1=cw-pd,k=Math.max(1,Math.round((in1+gc)/(ic+gc))),S=Math.floor(((in1+gc)/k-gc)*10)/10;c.style.setProperty('--S',S+'px');
 [].forEach.call(c.children,function(s){var w=fSpan(s);s.style.width=(cw*w+gp*(w-1))+'px';var h=s.offsetHeight,best=0,bt=1e9;
  for(var st=0;st+w<=n;st++){var t=Math.max.apply(null,H.slice(st,st+w));if(t<bt-1){bt=t;best=st}}
  s.style.left=best*(cw+gp)+'px';s.style.top=bt+'px';for(var q=best;q<best+w;q++)H[q]=bt+h+gp});
 c.style.height=Math.max(0,Math.max.apply(null,H)-gp)+'px';if(!c._a){c._a=1;requestAnimationFrame(function(){c.classList.add('an')})}}
function fSetSpan(k,w){FAVG[k].w=w;WS('favg',FAVG);var b=document.querySelector('#fbxs .bx[data-fg="'+k+'"] .wb');if(b){b.innerHTML='<i></i>'.repeat(w);b.title='Szélesség: '+w+' hasáb (kattints a váltáshoz)'}flay()}
$('fav').addEventListener('change',function(e){var k=e.target.dataset.fgn;if(k==null)return;FAVG[k].n=e.target.value.trim()||'Kedvenc doboz';WS('favg',FAVG)});
$('fav').addEventListener('keydown',function(e){if(e.target.dataset.fgn!=null&&e.key==='Enter')e.target.blur()});
$('fav').addEventListener('click',function(e){var b=e.target.closest('[data-fwb]');if(!b)return;var s=b.closest('.bx');fSetSpan(+b.dataset.fwb,fSpan(s)%nC()+1)});
var FB=null;
$('fav').addEventListener('pointerdown',function(e){if(e.button>0)return;var rz=e.target.closest('#fbxs .rz');
 if(rz){e.preventDefault();var s=rz.parentNode;FB={rz:true,s:s,k:+s.dataset.fg,on:true};s.classList.add('rs');document.body.classList.add('dragging');return}
 var h=e.target.closest('#fbxs .bxh,#fbxs .hd');if(!h||e.target.closest('input:focus,.x,.wb'))return;
 FB={s:h.closest('.bx'),x0:e.clientX,y0:e.clientY,on:false,touch:e.pointerType!=='mouse'};FB.tm=setTimeout(function(){if(FB&&!FB.on)fbStart()},FB.touch?380:250)});
function fbStart(){FB.on=true;FB.s.classList.add('mv');document.body.classList.add('dragging');var i=FB.s.querySelector('input');if(i)i.blur();if(navigator.vibrate)try{navigator.vibrate(15)}catch(e){}}
function fbMove(x,y){var c=$('fbxs');
 if(FB.rz){var n=nC(),gp=innerWidth<=640?14:22,cw=(c.clientWidth-(n-1)*gp)/n,r=FB.s.getBoundingClientRect(),w=Math.max(1,Math.min(n,Math.round((x-r.left+gp)/(cw+gp))));if(w!==fSpan(FB.s))fSetSpan(FB.k,w);return}
 var o=null;[].some.call(c.children,function(s){if(s===FB.s)return false;var r=s.getBoundingClientRect();if(x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom){o={s:s,r:r};return true}});
 if(o){var after=y>o.r.top+o.r.height/2,ref=after?o.s.nextSibling:o.s;if(ref!==FB.s&&FB.s.nextSibling!==ref){c.insertBefore(FB.s,ref);flay()}}
 var m=60;if(y<m)scrollBy(0,-12);else if(y>innerHeight-m)scrollBy(0,12)}
function fbEnd(){if(!FB)return;clearTimeout(FB.tm);if(FB.on){FB.s.classList.remove('mv','rs');document.body.classList.remove('dragging');noClick=true;setTimeout(function(){noClick=false},350);
  if(!FB.rz){var NG=[];document.querySelectorAll('#fbxs .bx').forEach(function(s){NG.push(FAVG[+s.dataset.fg])});FAVG=NG;WS('favg',FAVG);renderFav()}}FB=null}
addEventListener('pointermove',function(e){if(!FB)return;if(!FB.on){var dx=e.clientX-FB.x0,dy=e.clientY-FB.y0;if(dx*dx+dy*dy>64){if(FB.touch){clearTimeout(FB.tm);FB=null;return}fbStart()}else return}fbMove(e.clientX,e.clientY)});
addEventListener('pointerup',fbEnd);addEventListener('pointercancel',fbEnd);
addEventListener('touchmove',function(e){if(FB&&FB.on)e.preventDefault()},{passive:false});
var fl;addEventListener('resize',function(){clearTimeout(fl);fl=setTimeout(flay,80)});
$('sz').addEventListener('click',function(){setTimeout(flay,0)});$('oT').addEventListener('change',function(){setTimeout(flay,0)});$('oA').addEventListener('change',function(){setTimeout(flay,0)});
$('cols').addEventListener('click',function(){if(!$('fav').hidden)renderFav()});
// kedvencek atrendezese: lenyomva tartas (telefon) vagy huzas (eger), a celikon ele/moge kerul
var FD=null;
function fTgt(x,y){var t=pickT(x,y,'#fav',FD.id);FD.mode=t?t.mode:null;return t?t.li:null}
function fStart(){var a=FD.li.querySelector('.ic'),r=a.getBoundingClientRect(),g=document.createElement('div');g.id='ghost';g.style.setProperty('--gw',r.width+'px');
 var im=a.querySelector('img');g.innerHTML=im?'<img src="'+im.src+'" alt="">':'';if(!im)g.style.background='#456';document.body.appendChild(g);
 FD.g=g;FD.on=true;FD.li.classList.add('drag');document.body.classList.add('dragging');fMove(FD.x,FD.y);if(navigator.vibrate)try{navigator.vibrate(15)}catch(e){}}
function fMove(x,y){FD.x=x;FD.y=y;if(!FD.on)return;FD.g.style.left=x+'px';FD.g.style.top=y+'px';var li=fTgt(x,y);
 document.querySelectorAll('#fav .tgt').forEach(function(q){q.classList.remove('tgt')});FD.t=li;FD.bx=null;if(!li){var el=document.elementFromPoint(x,y),bx=el&&el.closest('#fbxs .bx');if(bx&&+bx.dataset.fg!==favG(FD.id)){FD.bx=bx;bx.classList.add('tgt')}}insMark(li?{li:li,mode:FD.mode}:null);if(li){if(FD.mode==='on')li.querySelector('.ic').classList.add('tgt');FD.after=FD.mode==='a'}
 var m=60;if(y<m)scrollBy(0,-12);else if(y>innerHeight-m)scrollBy(0,12)}
function fEnd(ok){if(!FD)return;clearTimeout(FD.tm);insMark(null);if(FD.on){FD.g.remove();FD.li.classList.remove('drag');document.body.classList.remove('dragging');noClick=true;setTimeout(function(){noClick=false},350);
  if(ok){var id=FD.id,from=favG(id);if(from>=0)FAVG[from].ids=FAVG[from].ids.filter(function(x){return x!==id});
  // ikon közepére: csoport (a célikon csoportjába, vagy új kedvenc doboz a kettőből) (Miske, 10-23 18:53)
  if(FD.t&&FD.mode==='on'){var to=+FD.t.dataset.id,k=favG(to);if(k>=0)FAVG[k].ids.splice(FAVG[k].ids.indexOf(to)+1,0,id);else FAVG.push({n:'Csoport '+(FAVG.length+1),ids:[to,id]})}
  else if(FD.t){var to=+FD.t.dataset.id,k=favG(to);if(k>=0)FAVG[k].ids.splice(FAVG[k].ids.indexOf(to)+(FD.after?1:0),0,id);else{FAV=FAV.filter(function(x){return x!==id});FAV.splice(FAV.indexOf(to)+(FD.after?1:0),0,id)}}
  else if(FD.bx){var kb=+FD.bx.dataset.fg;FAVG[kb].ids.push(id)}else if(from>=0){FAV=FAV.filter(function(x){return x!==id});FAV.push(id)}favSave()}renderFav()}FD=null}
$('fav').addEventListener('pointerdown',function(e){if(e.button>0||e.target.closest('.fx'))return;var li=e.target.closest('#fav li[data-id]');if(!li||!e.target.closest('.ic'))return;
 FD={li:li,id:+li.dataset.id,x:e.clientX,y:e.clientY,x0:e.clientX,y0:e.clientY,on:false,touch:e.pointerType!=='mouse'};FD.tm=setTimeout(function(){if(FD&&!FD.on)fStart()},FD.touch?420:300)});
addEventListener('pointermove',function(e){if(!FD)return;var dx=e.clientX-FD.x0,dy=e.clientY-FD.y0;if(!FD.on){if(dx*dx+dy*dy>64){if(FD.touch){clearTimeout(FD.tm);FD=null;return}fStart()}else return}fMove(e.clientX,e.clientY)});
addEventListener('pointerup',function(){fEnd(true)});addEventListener('pointercancel',function(){fEnd(false)});
addEventListener('touchmove',function(e){if(FD&&FD.on)e.preventDefault()},{passive:false});
addEventListener('contextmenu',function(e){if(e.target.closest&&e.target.closest('#fav .ic'))e.preventDefault()});
$('toList').onclick=function(){go('lista')};
$('back').onclick=function(){go('top')};
document.querySelector('header h1').onclick=function(){if($('main').hidden)go('top')};
$('ord').onclick=function(e){var v=e.target.dataset.v;if(!v)return;ORDL=v;WS('ord',v);renderList()};
$('q').oninput=function(){AF=null;renderList();renderArts()};
$('arts').onclick=function(e){var b=e.target.closest('[data-ar]');if(!b)return;AF=AF===b.dataset.ar?null:b.dataset.ar;$('q').value=AF||'';renderList();markArts();var y=$('years').getBoundingClientRect().top+scrollY-(innerWidth>640?80:10);scrollTo({top:y,behavior:'smooth'})};
$('years').onclick=function(e){var yb=e.target.closest('[data-yb]');if(yb){yBox(yb);return}var ar=e.target.closest('[data-ar]');if(ar){$('q').value=AF=ar.dataset.ar;renderList();markArts();var y=$('years').getBoundingClientRect().top+scrollY-(innerWidth>640?80:10);scrollTo({top:y,behavior:'smooth'});return}var a=e.target.closest('[data-p]');if(a){if(!ready||e.metaKey||e.ctrlKey||e.shiftKey)return;e.preventDefault();ORD=null;play('lst',+a.dataset.p);document.querySelectorAll('.sr2.on').forEach(function(x){x.classList.remove('on')});a.closest('.sr2').classList.add('on');return}var d=e.target.dataset;if(!d.a)return;var id=+d.a;FAV=FAV.indexOf(id)>=0?FAV.filter(function(x){return x!==id}):FAV.concat([id]);favSave();favN();var on=FAV.indexOf(id)>=0;e.target.classList.toggle('on',on);e.target.textContent=on?'★':'☆';e.target.title=on?'Levétel a kedvencek közül':'Kedvenceimhez';e.target.setAttribute('aria-label',e.target.title);
 var bx=e.target.closest('.yb'),yf=bx&&bx.querySelector('.yf');if(yf){var al=[].every.call(bx.querySelectorAll('.st[data-a]'),function(x){return x.classList.contains('on')});yf.classList.toggle('on',al);yf.textContent=al?'★':'☆'}};
var rz,rzw=innerWidth;addEventListener('resize',function(){if(innerWidth===rzw)return;rzw=innerWidth;clearTimeout(rz);rz=setTimeout(function(){if(!$('lista').hidden){renderArts();renderList()}else if(!$('fav').hidden)renderFav()},150)});
var isDark=function(){var t=document.documentElement.dataset.theme;return t?t==='dark':matchMedia('(prefers-color-scheme:dark)').matches};
var th=LS('theme',null);if(th==='dark'||th==='light')document.documentElement.dataset.theme=th;
$('bth').onclick=function(){var d=!isDark();document.documentElement.dataset.theme=d?'dark':'light';WS('theme',d?'dark':'light')};

/* a lejátszósáv ne takarja el az utolsó sort: az alsó térköz mindig a sáv magassága */
(function(){var dk=document.getElementById('dock');if(!dk)return;
 function fit(){var on=document.body.classList.contains('docked');document.body.style.paddingBottom=on?(dk.offsetHeight+28)+'px':''}
 if(window.ResizeObserver)new ResizeObserver(fit).observe(dk);
 new MutationObserver(fit).observe(document.body,{attributes:true,attributeFilter:['class']});addEventListener('resize',fit);fit()})();
// szam tovabbkuldese: mobilon a rendszer sajat megosztoja, maskor menu (Viber, WhatsApp, Messenger, Facebook, e-mail, link masolasa)
var OWN=window.isSecureContext&&/^https?:$/.test(location.protocol)&&window.top===window.self&&!/claude\.ai|claudeusercontent/.test(location.hostname);
function shareInfo(){var d=Q!=null&&DATA[Q]&&DATA[Q][cur];if(!d)return null;
 // a link a kuldo nezetet is viszi: oldal (nyitolap, kedvencek, valogato) es a valogatoban a szuro
 var v=!$('lista').hidden?'lista':!$('fav').hidden?'fav':'top',cx=v;if(v==='lista'){var q=$('q').value.trim();if(AF)cx+='.a.'+encodeURIComponent(AF);else if(q)cx+='.q.'+encodeURIComponent(q)}
 var url=OWN?location.origin+location.pathname.replace(/[^\/]*$/,'')+'d/'+d[3]+'.html?k=2#'+cx:(d[2]?'https://youtu.be/'+d[2]:'https://www.youtube.com/results?search_query='+encodeURIComponent(d[1]+' '+d[0]));
 return{title:d[0]+' – '+d[1],text:'„'+d[0]+'” – '+d[1]+' 🎵',url:url}}
// a szovegben ne legyen „IKONOK.HU”: a Viber linknek veszi, es az elso link (a fooldal) elonezetet mutatja (Miske, 10-23)
function shMenu(si){var o=$('shm');if(o){o.remove();return}si=si||shareInfo();if(!si)return;var t=encodeURIComponent(si.text+' '+si.url),u=encodeURIComponent(si.url);
 var m=document.createElement('div');m.id='shm';m.setAttribute('role','menu');
 m.innerHTML='<p>'+(si.site?'Küldd el az oldalt:':'Küldd tovább:')+' <b>'+esc(si.title)+'</b></p><div class="shl">'+
  // Viber: csak a puszta link ad kattinthato kepes elonezetet (Miske kiprobalta, 10-23); a link a vagolapra is kerul tartaleknak
  '<a role="menuitem" class="v" id="shv" href="viber://forward?text='+u+'"><i>V</i>Viber</a>'+  // csak a link, szoveg nelkul (Miske, 10-23 16:53)
  '<a role="menuitem" class="w" href="https://wa.me/?text='+t+'" target="_blank" rel="noopener"><i>W</i>WhatsApp</a>'+
  '<a role="menuitem" class="m" href="fb-messenger://share/?link='+u+'"><i>M</i>Messenger</a>'+
  '<a role="menuitem" class="f" href="https://www.facebook.com/sharer/sharer.php?u='+u+'" target="_blank" rel="noopener"><i>f</i>Facebook</a>'+
  '<a role="menuitem" class="e" href="mailto:?subject='+encodeURIComponent(si.title)+'&amp;body='+t+'"><i>@</i>E-mail</a>'+
  '<button type="button" role="menuitem" class="c" id="shc"><i>⧉</i>Link másolása</button></div><input id="shu" readonly value="'+esc(si.url)+'" aria-label="A szám linkje">';
 m.style.bottom=((document.body.classList.contains('docked')?$('dock').offsetHeight:0)+12)+'px';document.body.appendChild(m);$('shc').focus();
 var v=$('shv');if(v)v.addEventListener('click',function(){try{navigator.clipboard.writeText(si.url).catch(function(){})}catch(e){}var i=$('shu');if(i){i.select();try{document.execCommand('copy')}catch(e){}}
  m.querySelector('p').innerHTML='<b>✓ Elküldve a Vibernek.</b> Ha nem jelenik meg a kép, a link a vágólapon is ott van: <kbd>'+(/Mac/.test(navigator.platform||'')?'⌘':'Ctrl')+'</kbd> + <kbd>V</kbd>'})}
$('bSh').onclick=function(){var si=shareInfo();if(!si)return;
 // telefonon csak a linket adjuk at: ha szoveg is van mellette, a Viber elonezetenek kepe nem kattinthato; a cim es a kep az elonezetbol jon (Miske, 10-23)
 if(navigator.share&&matchMedia('(pointer:coarse)').matches){navigator.share({url:si.url}).catch(function(e){if(!e||e.name!=='AbortError')shMenu()});return}
 shMenu()};
document.addEventListener('click',function(e){var m=$('shm');if(!m)return;
 if(e.target.closest('#shc')){var v=$('shu').value,ok=function(){$('shc').innerHTML='<i>✓</i>Kimásolva'};
  try{navigator.clipboard.writeText(v).then(ok,function(){$('shu').select();ok()})}catch(x){$('shu').select();ok()}return}
 if(e.target.closest('#shm a')){setTimeout(function(){var q=$('shm');if(q)q.remove()},300);return}
 if(!e.target.closest('#shm,#bSh,#instS,#cfgSend'))m.remove()});
addEventListener('keydown',function(e){if(e.key==='Escape'){var m=$('shm');if(m)m.remove()}});
// tovabbkuldott link (#d<id>[.<oldal>[.a|q.<szuro>]]): ugyanaz a nezet nyilik meg a lejatszoval, mint a kuldonel
(function(){var m=location.hash.match(/^#d(\d+)(?:\.(top|fav|lista))?(?:\.([aq])\.(.+))?$/);if(!m||!BY[+m[1]])return;var id=+m[1],v=m[2]||'top';
 if(v==='fav'&&!FAV.length)v='top';
 if(v==='lista'){go('lista');if(m[3]){var f=decodeURIComponent(m[4]);if(m[3]==='a'&&ART.some(function(x){return x[0]===f})){AF=f;$('q').value=f}else{AF=null;$('q').value=f}renderList();renderArts();markArts()}}else go(v);
 var l=v==='lista'?'lst':v,i=-1;(DATA[l]||[]).some(function(d,k){if(d[3]===id){i=k;return true}});
 if(i<0){var s=BY[id];DATA.lnk=[[s[3],s[2],s[4]||'',s[0]]];NAME.lnk='Neked küldték';l='lnk';i=0}
 var ios=/iphone|ipad|ipod/i.test(navigator.userAgent)||(/Macintosh/.test(navigator.userAgent)&&navigator.maxTouchPoints>1);
 function tip(){var t=document.createElement('div');t.id='tip';t.setAttribute('role','status');t.innerHTML='<b>▶</b> Koppints a lejátszás gombra, és szól a dal!';t.style.bottom=($('dock').offsetHeight+14)+'px';document.body.appendChild(t);setTimeout(function(){t.classList.add('out')},5200);setTimeout(function(){t.remove()},6000)}
 // a böngészők hangos lejátszást csak koppintásra engednek: a címzett egy nagy „Lejátszás” kártyát kap, a koppintás indítja a dalt
 function card(){var s=BY[id],c=document.createElement('div');c.id='lnkc';c.setAttribute('role','dialog');c.setAttribute('aria-label','Neked küldött dal');
  c.innerHTML='<button type="button" class="lc">'+(ICON[id]?'<img src="ikon/'+id+'.webp" alt="">':'')+'<span class="lt">'+s[3].replace(/</g,'&lt;')+'</span><span class="la">'+s[2].replace(/</g,'&lt;')+'</span><span class="lp">▶ Lejátszás</span></button><button type="button" class="lx" aria-label="Bezárás">✕</button>';
  document.body.appendChild(c);c.querySelector('.lc').onclick=function(){c.remove();start()};c.querySelector('.lx').onclick=function(){c.remove()}}
 function start(){ORD=null;play(l,i);if(ios){setTimeout(function(){if(!playing){setPP(false);tip()}},1500)}else setTimeout(function(){if(!playing)tip()},3000);
  var li=document.querySelector((v==='lista'?'#years .pb[data-p="'+i+'"]':'#'+(v==='fav'?'fav':'main')+' li[data-id="'+id+'"]'));
  if(li&&l!=='lnk'){var r=li.getBoundingClientRect();if(r.top<0||r.bottom>innerHeight-$('dock').offsetHeight)scrollTo({top:scrollY+r.top-innerHeight/3})}
  if(v==='lista'&&l==='lst')document.querySelectorAll('#years .sr2').forEach(function(x){var p=x.querySelector('.pb');x.classList.toggle('on',!!p&&+p.dataset.p===i)})}
 card()})();
// a Beállításokban mindig elérhető a telepítési ajánlat (Miske, 10-23: az app törlése után nem jött vissza, mert korábban ✕-szel elrejtette)
(function(){var b=$('instAg');if(!b)return;if(matchMedia('(display-mode: standalone)').matches||navigator.standalone){$('instA').hidden=true;return}
 b.onclick=function(){WS('instx',0);location.hash='telepites';location.reload()}})();
// telepites: ha az oldal nincs telepitve, az oldal aljan felajanlja (Android/asztali Chrome: gomb; iPhone: utmutato)
(function(){var st=matchMedia('(display-mode: standalone)').matches||navigator.standalone,force=location.hash==='#telepites';
 if(st&&!force)return;var x=LS('instx',0);if(!force&&x&&Date.now()-x<7*864e5)return;
 var ua=navigator.userAgent,ios=/iphone|ipad|ipod/i.test(ua)||(/Macintosh/.test(ua)&&navigator.maxTouchPoints>1),mob=matchMedia('(pointer:coarse)').matches,dp=null;
 var el=document.createElement('aside');el.id='inst';el.hidden=true;el.setAttribute('aria-label','Telepítés');
 var desk=!ios&&!mob,site={site:1,title:'IKONOK.HU',text:'IKONOK.HU – a magyar slágerek ikonokban 🎵',url:OWN?location.origin+location.pathname.replace(/[^\/]*$/,''):'https://ikonok.hu/'};
 function dDraw(){var mac=/Mac/.test(navigator.platform||ua);el.innerHTML='<img src="'+document.querySelector('h1 img').src+'" alt="" width="56" height="56"><div class="it2"><b>Tetszik az IKONOK? Mentsd el, vagy küldd tovább!</b><span id="instH">Könyvjelzőhöz: <kbd>'+(mac?'⌘':'Ctrl')+'</kbd> + <kbd>D</kbd>'+(dp?', vagy telepítsd alkalmazásként.':'')+'</span></div><div class="ibt"><button type="button" class="pri" id="instS">Megosztás</button><button type="button" class="sec" id="instB">Könyvjelző</button><button type="button" class="sec" id="instC">Link másolása</button>'+(dp?'<button type="button" class="sec" id="instG">Telepítés</button>':'')+'</div><button type="button" class="x" id="instX" aria-label="Most nem" title="Most nem">✕</button>';el.hidden=false}
 function draw(){if(desk)return dDraw();el.innerHTML='<img src="'+document.querySelector('h1 img').src+'" alt="" width="56" height="56"><div class="it2"><b>Tedd ki az IKONOK-ot a kezdőképernyőre!</b><span>'+(dp?'Egy koppintással indul, mint egy alkalmazás, saját ablakban.':ios?'Safariban koppints alul a <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-label="Megosztás"><path d="M12 3v12M7 8l5-5 5 5M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg> Megosztás gombra, majd a „Főképernyőhöz adás” pontra.':'A böngésző menüjében (⋮) válaszd a „Hozzáadás a kezdőképernyőhöz” vagy „Alkalmazás telepítése” pontot.')+'</span></div>'+(dp?'<button type="button" class="pri" id="instG">Telepítés</button>':'')+'<button type="button" class="x" id="instX" aria-label="Most nem" title="Most nem">✕</button>';el.hidden=false}
 $('dock').parentNode.insertBefore(el,$('dock'));
 if(force)setTimeout(function(){if(!el.hidden)el.scrollIntoView({behavior:'smooth',block:'center'})},900);
 addEventListener('beforeinstallprompt',function(e){e.preventDefault();dp=e;draw()});
 addEventListener('appinstalled',function(){el.remove()});
 el.addEventListener('click',function(e){if(e.target.closest('#instX')){WS('instx',Date.now());el.remove();return}
  if(e.target.closest('#instS')){if(navigator.share&&!desk)navigator.share(site).catch(function(){});else shMenu(site);return}
  if(e.target.closest('#instB')){var h=$('instH');h.classList.remove('fl');void h.offsetWidth;h.classList.add('fl');return}
  if(e.target.closest('#instC')){var c=$('instC'),ok=function(){c.textContent='✓ Kimásolva'};try{navigator.clipboard.writeText(site.url).then(ok,function(){})}catch(x){}return}
  if(e.target.closest('#instG')&&dp){dp.prompt();dp.userChoice.then(function(c){if(c.outcome==='accepted')el.remove()});dp=null}});
 if(force||OWN)draw()})();
// lejatszo csillag: a szolo szam a Kedvenceimhez (ujra nyomva leveszi)
function favBtn(){var b=$('bFv'),d=Q!=null&&DATA[Q]&&DATA[Q][cur];if(!b||!d)return;var on=FAV.indexOf(d[3])>=0;b.textContent=on?'★':'☆';b.classList.toggle('on',on);b.title=on?'Levétel a kedvencek közül':'Kedvenceimhez';b.setAttribute('aria-label',on?'A szám levétele a kedvencek közül':'A szám a Kedvenceimhez');b.setAttribute('aria-pressed',on)}
$('bFv').onclick=function(){var d=Q!=null&&DATA[Q]&&DATA[Q][cur];if(!d)return;var id=d[3];
 var u=null;if(FAV.indexOf(id)>=0){u=favUndo('Levéve: '+BY[id][3]);FAV=FAV.filter(function(x){return x!==id})}else FAV.push(id);favSave();favN();favBtn();if(u)u();
 if(!$('fav').hidden&&Q!=='fav')renderFav();
 // a Valogato soraiban is frissuljon a csillag
 document.querySelectorAll('.st[data-a="'+id+'"]').forEach(function(x){var on=FAV.indexOf(id)>=0;x.classList.toggle('on',on);x.textContent=on?'★':'☆'})};
// lejátszó: az előadó nevére kattintva a Válogatóban az előadó összes száma (Miske, 10-23); a zene közben szól tovább
(function(){var a=$('mA');if(!a)return;a.setAttribute('role','button');a.tabIndex=0;a.title='Az előadó összes száma';
 function open(){var n=a.textContent.trim();if(!n||!ART.some(function(x){return x[0]===n}))return;go('lista');AF=n;$('q').value=n;renderList();renderArts();markArts();
  var y=$('years').getBoundingClientRect().top+scrollY-(innerWidth>640?80:10);scrollTo({top:y,behavior:'smooth'})}
 a.onclick=open;a.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();open()}}})();
// az ikon alatti előadónévre kattintva is az előadó összes száma (Miske, 10-23 14:15); a cím nem kattintható
document.addEventListener('click',function(e){var c=e.target.closest('#main .ica,#fav .ica');if(!c)return;var li=c.closest('li[data-id]'),s=li&&BY[li.dataset.id];if(!s)return;
 e.preventDefault();go('lista');AF=s[2];$('q').value=AF;renderList();renderArts();markArts();var y=$('years').getBoundingClientRect().top+scrollY-(innerWidth>640?80:10);scrollTo({top:y,behavior:'smooth'})});
// iPad/iPhone: ha a YouTube némán folytatja (pl. a rendszer megállította, majd némán indult újra), a lejátszó gombjai visszakapcsolják a hangot,
// és amíg néma, egy „Hang bekapcsolása” gomb látszik (Miske, 10-23 13:22)
(function(){function um(){try{if(P&&P.isMuted&&P.isMuted()){P.unMute();P.setVolume(100)}}catch(e){}}
 document.addEventListener('click',function(e){if(e.target.closest('#dock,#lnkc,.ic,#seq,#all'))setTimeout(um,0)},true);
 var b=document.createElement('button');b.type='button';b.id='bSnd';b.hidden=true;b.innerHTML='🔇 Koppints ide a hangért';b.onclick=function(){um();b.hidden=true;try{if(P.getPlayerState()!==1)P.playVideo()}catch(e){}};
 document.body.appendChild(b);
 setInterval(function(){var m=false;try{m=document.body.classList.contains('docked')&&P&&P.isMuted&&P.isMuted()&&P.getPlayerState()===1}catch(e){}
  if(m){var d=$('dock');b.style.bottom=((d?d.offsetHeight:0)+14)+'px'}b.hidden=!m},1000)})();
// kevert mód a lejátszóban (Miske, 10-23 17:03): be/ki kapcsolható gomb; bekapcsolva a mostani szám végigszól, utána az adott doboz
// (nyitólap/kedvencek doboza, válogató éve) dalai jönnek véletlen sorrendben. A fejléc Kevert gombja is bekapcsolja, a Lejátszás kikapcsolja.
(function(){var nx=$('bNext');if(!nx)return;var SHF=false,b=document.createElement('button');b.type='button';b.id='bShf';b.setAttribute('aria-label','Kevert lejátszás');b.title='Kevert lejátszás (az adott dobozból)';b.setAttribute('aria-pressed','false');
 b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h3.5c2 0 3.2.9 4.3 2.6l2.4 4.8c1.1 1.7 2.3 2.6 4.3 2.6H21M3 17h3.5c2 0 3.2-.9 4.3-2.6M13.2 9.6c1.1-1.7 2.3-2.6 4.3-2.6H21M18 4l3 3-3 3M18 14l3 3-3 3"/></svg>';nx.parentNode.insertBefore(b,nx.nextSibling);
 function boxIdx(){var all=(DATA[Q]||[]).map(function(_,i){return i}),d=DATA[Q]&&DATA[Q][cur];if(!d)return all;
  if(Q==='top'||Q==='fav'){var li=document.querySelector('#'+(Q==='fav'?'fav':'main')+' li[data-id="'+d[3]+'"]'),bx=li&&(li.closest('.bx')||li.closest('.grid'));if(bx)return[].map.call(bx.querySelectorAll('.ic[data-i]'),function(a){return+a.dataset.i})}
  if(Q==='lst'){var p=document.querySelector('#years .pb[data-p="'+cur+'"]'),yb=p&&p.closest('.yb');if(yb)return[].map.call(yb.querySelectorAll('.pb[data-p]'),function(a){return+a.dataset.p})}
  return all}
 function build(){var ix=boxIdx().filter(function(i){return i!==cur});for(var i=ix.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=ix[i];ix[i]=ix[j];ix[j]=t}ORD=[cur].concat(ix);pos=0}
 function ui(){b.classList.toggle('on',SHF);b.setAttribute('aria-pressed',String(SHF));var m=$('mPos');if(m)m.textContent=m.textContent.replace(/ · keverve$/,'')+(SHF?' · keverve':'')}
 b.onclick=function(){SHF=!SHF;if(SHF){if(Q!=null&&cur>=0)build()}else ORD=null;ui()};
 // a kifejezett „sorban” gombok (fejléc Lejátszás, doboz ▶) kikapcsolják, a kevert gombok bekapcsolják; ikonra bökve a mód marad
 document.addEventListener('click',function(e){if(!e.target.closest)return;if(e.target.closest('#seq,[data-yb="p"],[data-af="p"]')){SHF=false;ui()}else if(e.target.closest('#all,[data-yb="s"],[data-af="s"]')){SHF=true;ui()}},true);
 var _pl=play;play=function(l,i){if(!SHF&&ORD)SHF=true;_pl(l,i);if(SHF&&!ORD&&cur>=0)build();ui()}})();
// egységes függőleges térközök (Miske, 10-23 17:05, 17:09: akkora, mint a doboz és a képernyőszél közti hely, gépen max 24): oldal teteje → logó/gombok, fejléc alja → fülek, fülek alja → doboz mind ugyanakkora,
// a fülek és a doboz közti távolság (mobil 18, gép 24 px). A fejléc magassága betűtől/gomboktól függ, ezért mérve állítjuk.
(function(){var hd=document.querySelector('header'),tb=$('tabs');if(!hd||!tb)return;
 function fix(){var bx=$('bxs'),G=24,y=scrollY;if(bx&&bx.offsetParent)G=Math.min(24,Math.round(bx.getBoundingClientRect().left));hd.style.marginTop='0px';tb.style.marginTop='0px';tb.style.marginBottom=G+'px';
  var els=[].slice.call(hd.querySelectorAll('h1 img,.acts')).filter(function(e){return e.offsetParent}),top=1e9,bot=0;
  els.forEach(function(e){var r=e.getBoundingClientRect();top=Math.min(top,r.top+y);bot=Math.max(bot,r.bottom+y)});if(!els.length)return;
  hd.style.marginTop=(G-top)+'px';bot+=G-top;var t=tb.querySelector('.tabs')||tb,tt=t.getBoundingClientRect().top+y;tb.style.marginTop=(G-(tt-bot))+'px'}
 fix();addEventListener('load',fix);addEventListener('resize',fix);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fix)})();
// Beállítások átvitele linkben (Miske, 10-23 18:46): a Beállításokban linket ad a mostani beállításokról (kedvencek, dobozok, nyitólap, méret, téma).
// A link (#cfg=...) a másik gépen rákérdez, milyen néven mentse a kapott beállítást; a régi is elmentődik, és a Beállításokban vissza lehet rá váltani.
(function(){
 // a nyitólap aljára: küldés gomb + mentett beállítások listája (Miske, 10-23 18:47: lista a nyitólap alján, átnevezés, megerősítéses törlés)
 var mn=$('main');if(mn&&!$('cfgBox')){var sc=document.createElement('section');sc.id='cfgBox';sc.setAttribute('aria-label','Beállítások');
  sc.innerHTML='<div class="cfgh"><h2>Beállításaim</h2><span class="grow"></span><button type="button" class="sec" id="cfgSave" title="A mostani beállítás mentése külön változatként">＋ Mentés új néven</button><button type="button" class="sec" id="cfgSend"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:6px"><path d="M12 3v12M7 8l5-5 5 5M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"></path></svg>Küldés linkben</button></div><p class="hint" id="cfgMsg" hidden></p><ul id="cfgList"></ul>';
  mn.parentNode.insertBefore(sc,mn.nextSibling)}
 var KEYS=['fav','favg','frissdel','grp','home','homet','loose','opt','ord','theme','notxt','txtv'];
 function snap(){var o={};KEYS.forEach(function(k){try{var v=localStorage.getItem(k);if(v!==null)o[k]=JSON.parse(v)}catch(e){}});return o}
 function put(o){KEYS.forEach(function(k){try{if(k in o)localStorage.setItem(k,JSON.stringify(o[k]));else localStorage.removeItem(k)}catch(e){}})}
 function now(){var d=new Date(),z=function(n){return(n<10?'0':'')+n};return d.getFullYear()+'.'+z(d.getMonth()+1)+'.'+z(d.getDate())+'. '+z(d.getHours())+':'+z(d.getMinutes())}
 function saved(){return LS('mentett',[])}
 function keep(n,d){var L=saved().filter(function(x){return x.n!==n});L.unshift({n:n,t:now(),d:d});WS('mentett',L.slice(0,20))}
 function b64(u8){var s='';for(var i=0;i<u8.length;i+=8192)s+=String.fromCharCode.apply(null,u8.subarray(i,i+8192));return btoa(s).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
 function unb64(t){t=t.replace(/-/g,'+').replace(/_/g,'/');var s=atob(t),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return u}
 function pipe(u8,T){return new Response(new Blob([u8]).stream().pipeThrough(T)).arrayBuffer().then(function(b){return new Uint8Array(b)})}
 function enc(o){var u=new TextEncoder().encode(JSON.stringify(o));if(window.CompressionStream)return pipe(u,new CompressionStream('deflate-raw')).then(function(z){return'z'+b64(z)});return Promise.resolve('j'+b64(u))}
 function dec(t){var u=unb64(t.slice(1));return(t[0]==='z'?pipe(u,new DecompressionStream('deflate-raw')):Promise.resolve(u)).then(function(x){return JSON.parse(new TextDecoder().decode(x))})}
 var base=/^https?:$/.test(location.protocol)&&!/claude|anthropic|usercontent/.test(location.hostname)?location.origin+location.pathname:'https://ikonok.hu/';
 function msg(h){var m=$('cfgMsg');if(m){m.hidden=false;m.innerHTML=h}}
 var sb=$('cfgSend');if(sb)sb.onclick=function(){enc(snap()).then(function(t){var url=base+'#cfg='+t;
  // ugyanaz az alkalmazásválasztó, mint a dal továbbküldésénél (Miske, 10-23 19:10): telefonon a rendszer megosztója, gépen a Viber/WhatsApp/… menü
  var si={title:'IKONOK beállításaim',text:'Az IKONOK.HU beállításaim (kedvencek, dobozok, elrendezés):',url:url};
  if(navigator.share&&matchMedia('(pointer:coarse)').matches){navigator.share({url:url}).catch(function(e){if(!e||e.name!=='AbortError')shMenu(si)});return}
  var o=$('shm');if(o)o.remove();shMenu(si)})};
 function list(){var ul=$('cfgList');if(!ul)return;var L=saved(),a=LS('aktnev','');
  ul.innerHTML=L.length?L.map(function(x,i){return'<li'+(x.n===a?' class="akt"':'')+'><span class="cn"><b>'+esc(x.n)+'</b> <small>'+esc(x.t)+(x.n===a?' · ez van betöltve':'')+'</small></span><span class="grow"></span>'+(x.n===a?'':'<button type="button" class="sec" data-cl="'+i+'">Betöltés</button>')+'<button type="button" class="sec" data-cr="'+i+'" title="Átnevezés" aria-label="Átnevezés">✎</button><button type="button" class="sec" data-cx="'+i+'" aria-label="Törlés" title="Törlés">✕</button></li>'}).join(''):'';
  // a mostani (még névtelen) beállítás is látszik (Miske, 10-23 19:36: az üres lista zavaró volt)
  if(!a||!L.some(function(x){return x.n===a}))ul.insertAdjacentHTML('afterbegin','<li class="akt"><span class="cn"><b>Mostani beállítás</b> <small>még nincs elnevezve · ez van betöltve</small></span><button type="button" class="sec" data-cs="1">Elnevezés</button></li>')}
 list();
 function saveAs(){var n=prompt('Milyen néven mentsem el a mostani beállítást?','Saját beállítás ('+now()+')');if(n==null)return;n=n.trim().slice(0,40);if(!n)return;
  if(saved().some(function(x){return x.n===n})&&!confirm('Már van „'+n+'” nevű mentett beállítás. Felülírjam?'))return;keep(n,snap());WS('aktnev',n);list()}
 var svb=$('cfgSave');if(svb)svb.onclick=saveAs;
 var ul=$('cfgList');if(ul)ul.onclick=function(e){var b=e.target.closest('[data-cl],[data-cx],[data-cr],[data-cs]');if(!b)return;if(b.dataset.cs){saveAs();return}var L=saved(),a=LS('aktnev','');
  if(b.dataset.cx!=null){var x=L[+b.dataset.cx];if(x&&confirm('Biztosan törlöd a „'+x.n+'” mentett beállítást?')){L.splice(+b.dataset.cx,1);WS('mentett',L);list()}return}
  if(b.dataset.cr!=null){var x=L[+b.dataset.cr];if(!x)return;var n=prompt('Új név:',x.n);if(n==null)return;n=n.trim().slice(0,40);if(!n||n===x.n)return;
   if(L.some(function(y){return y.n===n})){alert('Már van ilyen nevű mentett beállítás.');return}if(a===x.n)WS('aktnev',n);x.n=n;WS('mentett',L);list();return}
  var x=L[+b.dataset.cl];if(!x)return;if(a)keep(a,snap());else keep('Előző beállítás ('+now()+')',snap());put(x.d);WS('aktnev',x.n);location.reload()};
 // a betöltött (aktív) változat mindig a legfrissebb állapotot tárolja: kilépéskor / elrejtéskor frissül
 addEventListener('pagehide',function(){var a=LS('aktnev','');if(!a)return;var L=saved(),x=L.filter(function(y){return y.n===a})[0];if(x){x.d=snap();WS('mentett',L)}});
 document.addEventListener('visibilitychange',function(){if(document.hidden)dispatchEvent(new Event('pagehide'))});
 // bejövő link
 addEventListener('hashchange',function(){if(/^#cfg=/.test(location.hash))location.reload()});
 var m=location.hash.match(/^#cfg=([zj][A-Za-z0-9_-]+)$/);if(!m)return;
 try{history.replaceState(null,'',location.pathname+location.search)}catch(e){}
 dec(m[1]).then(function(o){if(!o||typeof o!=='object')throw 0;
  var a=LS('aktnev',''),d=document.createElement('dialog');d.id='cfgDlg';
  d.innerHTML='<form method="dialog" class="dlg"><div class="dh"><h2>Beállítás érkezett</h2></div><p>Egy másik gépről küldött beállítást nyitottál meg (kedvencek, dobozok, nyitólap, méret, téma). Milyen néven mentsem el?</p><p><input id="cfgN" type="text" maxlength="40" style="width:100%;box-sizing:border-box;font:inherit;padding:10px 12px;border-radius:12px;border:1px solid var(--line);background:var(--bg);color:var(--fg)" value="Küldött beállítás ('+now()+')"></p><p class="hint">A mostani beállításodat is elmentem'+(a?' „'+esc(a)+'” néven':'')+', a nyitólap alján, a Beállításaim listában bármikor visszaválthatsz rá.</p><div class="dacts"><button class="sec" value="x">Mégse</button><span class="grow"></span><button class="pri okb" value="ok">Betöltés</button></div></form>';
  document.body.appendChild(d);d.addEventListener('close',function(){if(d.returnValue!=='ok'){d.remove();return}
   var n=($('cfgN').value||'').trim()||'Küldött beállítás ('+now()+')';keep(a&&a!==n?a:'Előző beállítás ('+now()+')',snap());keep(n,o);put(o);WS('aktnev',n);location.reload()});
  d.showModal();setTimeout(function(){var i=$('cfgN');i.focus();i.select()},50)}).catch(function(){alert('Ez a beállítás-link sérült vagy hiányos, nem tudom betölteni.')})})();
// Évek sikerlistái a nyitólap alján (Miske, 10-24 08:37; 08:51: a „C” változat): oldalra húzható évsáv, alatta a kiválasztott év ▶ (sorban) és kevert gombja; az év dalai sikerindex szerint
(function(){var mn=$('main');if(!mn||$('evBox'))return;var Y={};
 ALL.forEach(function(s){if(!s[1]||!s[4])return;(Y[s[1]]=Y[s[1]]||[]).push(s)});var ys=Object.keys(Y).sort();if(!ys.length)return;
 var PL='<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2v12l10-6z" fill="currentColor"/></svg>',SH='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h3.5c2 0 3.2.9 4.3 2.6l2.4 4.8c1.1 1.7 2.3 2.6 4.3 2.6H21M3 17h3.5c2 0 3.2-.9 4.3-2.6M13.2 9.6c1.1-1.7 2.3-2.6 4.3-2.6H21M18 4l3 3-3 3M18 14l3 3-3 3"/></svg>';
 var sel=String(LS('evsel',ys[ys.length-1]));if(!Y[sel])sel=ys[ys.length-1];
 var sc=document.createElement('section');sc.id='evBox';sc.setAttribute('aria-label','Évek sikerlistái');
 sc.innerHTML='<h2>Évek sikerlistái</h2><div class="evs" role="listbox" aria-label="Év">'+ys.map(function(y){return'<button type="button" class="evp" role="option" data-y="'+y+'">'+y+'</button>'}).join('')+'</div><div class="evr"><b id="evT"></b><span class="evb"><button type="button" data-ey="p" title="A kiválasztott év sikerlistája sorban" aria-label="Lejátszás sorban">'+PL+'</button><button type="button" data-ey="s" title="A kiválasztott év sikerlistája keverve" aria-label="Lejátszás keverve">'+SH+'</button></span></div>';
 mn.parentNode.insertBefore(sc,mn.nextSibling);
 var bar=sc.querySelector('.evs');
 function pick(y,scroll){sel=y;WS('evsel',y);bar.querySelectorAll('.evp').forEach(function(b){var on=b.dataset.y===y;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $('evT').textContent=y+' slágerei · '+Y[y].length+' dal';
  if(scroll){var b=bar.querySelector('[data-y="'+y+'"]');if(b)bar.scrollLeft=b.offsetLeft-bar.clientWidth/2+b.offsetWidth/2}}
 pick(sel,false);requestAnimationFrame(function(){pick(sel,true)});
 // egérgörgővel is oldalra megy (gépen)
 bar.addEventListener('wheel',function(e){if(Math.abs(e.deltaY)>Math.abs(e.deltaX)){bar.scrollLeft+=e.deltaY;e.preventDefault()}},{passive:false});
 sc.onclick=function(e){var p=e.target.closest('.evp');if(p){pick(p.dataset.y,false);return}
  var b=e.target.closest('[data-ey]');if(!b)return;var L=Y[sel].slice().sort(function(a,c){return(c[5]||0)-(a[5]||0)});
  DATA.ev=L.map(function(s){return[s[3],s[2],s[4]||'',s[0]]});NAME.ev=sel+' slágerei';
  if(!ready){window.open('https://www.youtube.com/watch?v='+L[0][4],'_blank');return}
  if(b.dataset.ey==='s')shuffle('ev');else{ORD=null;play('ev',0)}};
 // a lejátszó kevert-kapcsolója kövesse: ▶ = sorban, kevert = keverve
 document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-ey]');if(!b)return;var k=$('bShf');if(!k)return;var on=b.dataset.ey==='s';if(k.classList.contains('on')!==on)setTimeout(function(){if(k.classList.contains('on')!==on)k.click()},0)},true)})();
// telefonon rövidebb keresőfelirat, hogy kiférjen a „Válogató” cím mellett (10-24)
(function(){var q=$('q');if(!q)return;var L=q.placeholder;function f(){q.placeholder=innerWidth<=640?'Előadó vagy cím…':L}f();addEventListener('resize',f)})();
// Válogató: a piros kijelölés kövesse a lejátszott számot (következő/előző, automatikus továbblépés, kevert), és a lista görögjön oda, kb. a képernyő közepére (Miske, 10-24 09:12)
(function(){var _p=play;play=function(l,i){_p(l,i);try{mk()}catch(e){}};
 function mk(){var d=Q!=null&&DATA[Q]&&DATA[Q][cur];if(!d)return;var st=document.querySelector('#years .st[data-a="'+d[3]+'"]'),row=st&&st.closest('.sr2');
  document.querySelectorAll('#years .sr2.on').forEach(function(x){if(x!==row)x.classList.remove('on')});if(!row)return;row.classList.add('on');
  if(!$('lista').hidden){var r=row.getBoundingClientRect(),dk=document.body.classList.contains('docked')&&$('dock')?$('dock').offsetHeight:0,mid=(innerHeight-dk)/2;
   if(r.top<70||r.bottom>innerHeight-dk-20||Math.abs(r.top+r.height/2-mid)>innerHeight*.3)scrollTo({top:scrollY+r.top+r.height/2-mid,behavior:'smooth'})}}})();
// Nyitólap: ikonos ↔ szöveges (Válogató-szerű) nézet kapcsoló a fülsor bal oldalán (Miske, 10-24 09:14). A csoportok, dobozok, húzás, lejátszás ugyanúgy működnek.
(function(){var tb=$('tabs');if(!tb||$('tvB'))return;var b=document.createElement('button');b.type='button';b.id='tvB';tb.insertBefore(b,tb.firstChild);
 var IL='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
  IG='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></svg>';
 function set(on,save){document.body.classList.toggle('txtv',on);if(save)WS('txtv',on?1:0);b.innerHTML=on?IG+'<span>Ikonok</span>':IL+'<span>Lista</span>';b.title=on?'Váltás ikonos nézetre':'Váltás szöveges (listás) nézetre';b.setAttribute('aria-pressed',on);
  setTimeout(function(){try{lay();fitAll()}catch(e){}try{if(!$('fav').hidden)renderFav()}catch(e){}},0)}
 set(!!LS('txtv',0),false);b.onclick=function(){set(!document.body.classList.contains('txtv'),true)}})();
// A dal egymondatos összefoglalója a lejátszó alatt (Miske, 10-24 09:16)
(function(){var m=document.querySelector('#dock .dk');if(!m||$('mD'))return;var p=document.createElement('p');p.id='mD';p.hidden=true;m.parentNode.insertBefore(p,m.nextSibling);
 var _p=play;play=function(l,i){_p(l,i);try{var d=DATA[l]&&DATA[l][i],t=d&&typeof DESC!=='undefined'&&DESC[d[3]];p.textContent=t||'';p.hidden=!t;var y=d&&BY[d[3]]&&BY[d[3]][1];if(y){var e=document.createElement('span');e.className='mY';e.textContent=y;$('mT').appendChild(e)}}catch(e){}}})();
// Ország- és nyelvválasztó (Miske, 10-24 10:11): egyelőre csak Magyarország / magyar, a többi „hamarosan”
(function(){function menu(btn,kind){var o=$('lcm');if(o){var same=o.dataset.k===kind;o.remove();if(same)return}
 var h=kind==='c'?'<h4>Ország</h4><div class="it on">🇭🇺 <span>Magyarország</span></div><div class="it so">🌍 <span>További országok</span> <small>hamarosan</small></div>':'<h4>Nyelv</h4><div class="it on">Magyar</div><div class="it so">Más nyelvek <small>hamarosan</small></div>';
 o=document.createElement('div');o.id='lcm';o.dataset.k=kind;o.setAttribute('role','menu');o.innerHTML=h;document.body.appendChild(o);
 var r=btn.getBoundingClientRect();o.style.top=(r.bottom+scrollY+8)+'px';o.style.left=Math.max(8,Math.min(innerWidth-o.offsetWidth-8,r.right+scrollX-o.offsetWidth))+'px'}
 var c=$('bCountry'),l=$('bLang');if(!c||!l)return;c.onclick=function(e){e.stopPropagation();menu(c,'c')};l.onclick=function(e){e.stopPropagation();menu(l,'l')};
 document.addEventListener('click',function(e){var o=$('lcm');if(o&&!o.contains(e.target))o.remove()});document.addEventListener('keydown',function(e){if(e.key==='Escape'){var o=$('lcm');if(o)o.remove()}})})();
// Kedvenceim, érintőképernyő: a ✕ csak hosszú lenyomás után látszik, a következő máshová koppintásig (Miske, 10-24 10:14)
(function(){var t=null,x0=0,y0=0;
 document.addEventListener('pointerdown',function(e){if(e.target.closest&&e.target.closest('.fx'))return;document.body.classList.remove('fxedit');clearTimeout(t);
  if(e.pointerType==='mouse'||!e.target.closest||!e.target.closest('#fav .ic'))return;x0=e.clientX;y0=e.clientY;t=setTimeout(function(){document.body.classList.add('fxedit')},420)},true);
 addEventListener('pointermove',function(e){if(t&&!document.body.classList.contains('fxedit')){var dx=e.clientX-x0,dy=e.clientY-y0;if(dx*dx+dy*dy>64){clearTimeout(t);t=null}}},true);
 addEventListener('pointerup',function(){if(!document.body.classList.contains('fxedit')){clearTimeout(t);t=null}},true)})();
// Összefoglaló ki/be gomb a lejátszóban (Miske, 10-24 10:17); állapot: localStorage 'desc' (alapból be)
(function(){var sh=$('bShf')||$('bNext');if(!sh||$('bDs'))return;var b=document.createElement('button');b.type='button';b.id='bDs';
 b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2.5"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>';
 var fv=$('bFv');if(fv)fv.parentNode.insertBefore(b,fv);else sh.parentNode.insertBefore(b,sh.nextSibling);
 function upd(){var on=LS('desc',1)!==0;document.body.classList.toggle('nodesc',!on);b.classList.toggle('on',on);b.setAttribute('aria-pressed',on);var t=on?'A dal összefoglalójának elrejtése':'A dal összefoglalójának megjelenítése';b.title=t;b.setAttribute('aria-label',t)}
 b.onclick=function(){WS('desc',LS('desc',1)!==0?0:1);upd()};upd()})();
// A lejátszott szám követése a Nyitólapon és a Kedvenceimben is: ha a sora/ikonja kilóg a képből, középre görget (Miske, 10-24 10:30)
(function(){var _p=play;play=function(l,i){_p(l,i);try{fol(l,i)}catch(e){}};
 function fol(l,i){if(l==='lst'||l==='ev')return;var d=DATA[l]&&DATA[l][i];if(!d)return;var sec=!$('main').hidden?$('main'):!$('fav').hidden?$('fav'):null;if(!sec)return;
  var a=sec.querySelector('a.ic[data-i="'+i+'"]');var li=a&&a.closest('li[data-id="'+d[3]+'"]')||sec.querySelector('li[data-id="'+d[3]+'"]');if(!li)return;
  var r=li.getBoundingClientRect(),dk=$('dock'),dh=dk&&document.body.classList.contains('docked')?dk.getBoundingClientRect().height:0,top=innerWidth>640?70:10,bot=innerHeight-dh;
  if(r.top>=top&&r.bottom<=bot)return;var y=r.top+scrollY-top-(bot-top)/2+r.height/2;scrollTo({top:Math.max(0,y),behavior:'smooth'})}})();
// Többnyelvű kezelőfelület (Miske, 10-24 10:32): a magyar szövegeket futás közben cseréli a kiválasztott nyelvre (i18n/<kód>.json, a kulcsok az I18K).
// Az előadó, a cím, a dobozok saját nevei és az évszámok érintetlenek maradnak. Nyelv: localStorage 'lang', első látogatáskor a böngésző nyelve, ha van fordítás.
(function(){if(typeof I18K==='undefined'||typeof I18L==='undefined')return;
 var SKIP='.ict,.ica,.icy,.tx,.arl,#mT,#mA,#mD,#mPos,.rk,#arts,.evs,a.ic,#live,script,style,svg,#years .yb h3,#bld,kbd,#cfgList .cn b,.afl b,#lcm .lnm,h1 .lt>span:first-child';
 var LANG='hu',TR=null,EX={},PAT=[],TN=new WeakMap(),AT=new WeakMap(),busy=false,ATTR=['title','aria-label','placeholder'];
 var AVAIL={};I18L.forEach(function(x){AVAIL[x[0]]=x});
 function norm(s){return s.replace(/\s+/g,' ').trim()}
 function build(arr){EX={};PAT=[];I18K.forEach(function(k,i){var t=arr[i];if(t==null||t==='')return;if(k.indexOf('{0}')>=0){var re=new RegExp('^'+k.replace(/[.*+?^$()|[\]\\]/g,'\\$&').replace(/\{(\d)\}/g,'(.+?)')+'$');PAT.push([re,t])}else EX[k]=t})}
 function tr(s){if(LANG==='hu'||!s)return s;var n=norm(s);if(!n)return s;var t=EX[n];if(t!=null)return s.replace(n,t);for(var i=0;i<PAT.length;i++){var m=n.match(PAT[i][0]);if(m){var o=PAT[i][1].replace(/\{(\d)\}/g,function(_,d){return m[+d+1]});return s.replace(n,o)}}return s}
 window.T=function(s){return tr(s)};
 function skip(el){return !el||(el.closest&&el.closest(SKIP))}
 function doText(n){var e=n.parentElement;if(skip(e))return;var o=TN.get(n);if(o==null||(n.nodeValue!==o.out)){o={hu:n.nodeValue};TN.set(n,o)}var v=LANG==='hu'?o.hu:tr(o.hu);o.out=v;if(n.nodeValue!==v)n.nodeValue=v}
 function doAttr(e){if(skip(e))return;var m=AT.get(e);if(!m){m={};AT.set(e,m)}ATTR.forEach(function(a){if(!e.hasAttribute(a))return;var c=e.getAttribute(a),r=m[a];if(!r||c!==r.out){r={hu:c};m[a]=r}var v=LANG==='hu'?r.hu:tr(r.hu);r.out=v;if(c!==v)e.setAttribute(a,v)})}
 function pat(k){var i=I18K.indexOf(k);return LANG==='hu'||!TR||!TR[i]?k:TR[i]}
 function special(root){
  var tl=$('toList'),na=$('nAll');if(tl&&na){var n=na.textContent,p=pat('Válogató ({0} szám)').split('{0}'),want=esc(p[0])+'<span id="nAll">'+esc(n)+'</span>'+esc(p[1]||'');if(tl.innerHTML!==want)tl.innerHTML=want}
  document.querySelectorAll('.bxh input').forEach(function(i){if(i===document.activeElement)return;if(!i.dataset.hu){if(i.value!=='Mostanában slágerek'&&i.value!=='Mindenkori Top 100')return;i.dataset.hu=i.value}
   if(i.value!==i.dataset.hu&&i.value!==i.dataset.tr){delete i.dataset.hu;delete i.dataset.tr;return}var v=LANG==='hu'?i.dataset.hu:tr(i.dataset.hu);i.dataset.tr=v;if(i.value!==v)i.value=v});
  var af=document.querySelector('#afbar .afl'),b=af&&af.querySelector('b');if(b){var m=af.textContent.match(/\((\d+)\)\s*$/);if(m){var q=pat('Csak {0} számai ({1})').split('{0}'),want2=esc(q[0])+'<b>'+esc(b.textContent)+'</b>'+esc((q[1]||'').replace('{1}',m[1]));if(af.innerHTML!==want2)af.innerHTML=want2}}}
 function walk(root){busy=true;try{if(root.nodeType===3){doText(root);return}var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT),n;while(n=w.nextNode())doText(n);if(root.querySelectorAll){if(root.hasAttribute&&ATTR.some(function(a){return root.hasAttribute(a)}))doAttr(root);root.querySelectorAll('[title],[aria-label],[placeholder]').forEach(doAttr)}special(root)}finally{busy=false}}
 var mo=new MutationObserver(function(ms){if(busy)return;var set=new Set();ms.forEach(function(m){if(m.type==='childList')m.addedNodes.forEach(function(x){set.add(x)});else if(m.type==='characterData')set.add(m.target);else set.add(m.target)});
  busy=true;try{set.forEach(function(x){if(x.nodeType===3)doText(x);else if(x.nodeType===1){var w=document.createTreeWalker(x,NodeFilter.SHOW_TEXT),n;while(n=w.nextNode())doText(n);if(ATTR.some(function(a){return x.hasAttribute(a)}))doAttr(x);x.querySelectorAll('[title],[aria-label],[placeholder]').forEach(doAttr)}});special(document.body)}finally{busy=false}if(typeof qTabs==='function')qTabs()});
 var _pr=window.prompt,_cf=window.confirm,_al=window.alert;window.prompt=function(m,d){return _pr.call(window,tr(m),d!=null?tr(String(d)):d)};window.confirm=function(m){return _cf.call(window,tr(m))};window.alert=function(m){return _al.call(window,tr(m))};
 function apply(code,arr){LANG=code;TR=arr;if(arr)build(arr);var d=AVAIL[code]||['hu','Magyar','ltr'];document.documentElement.lang=code;document.documentElement.dir=d[2];document.body.classList.toggle('nohu',code!=='hu');
  var lb=document.querySelector('#bLang svg text');if(lb)lb.textContent=code.toUpperCase().slice(0,3);document.title=code==='hu'?'IKONOK.HU':'IKONOK.HU – '+tr('IKONOK.HU – a magyar slágerek ikonokban 🎵').replace(/^IKONOK\.HU\s*[–-]\s*/,'').replace(/\s*🎵$/,'');walk(document.body);qTabs()}
 function load(code){if(code==='hu'||!AVAIL[code]){apply('hu',null);return Promise.resolve()}return fetch('i18n/'+code+'.json').then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(a){apply(code,a)}).catch(function(){apply('hu',null)})}
 // Fülek: hosszú feliratnál (pl. grúz) kisebb betű, hogy ne csonkuljon és ne takarja a ☰ gombot
 var ftq=0;function fitTabs(){var bs=document.querySelectorAll('#tabs .tabs button');if(!bs.length)return;bs.forEach(function(b){b.style.fontSize='';b.style.paddingLeft=b.style.paddingRight=''});
  var f=parseFloat(getComputedStyle(bs[0]).fontSize),rg=document.createRange(),over=function(){for(var i=0;i<bs.length;i++){var b=bs[i],cs=getComputedStyle(b);rg.selectNodeContents(b);if(rg.getBoundingClientRect().width>b.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight)+.5)return true}return false};
  if(over())bs.forEach(function(b){b.style.paddingLeft=b.style.paddingRight='9px'});while(f>11&&over()){f-=.5;bs.forEach(function(b){b.style.fontSize=f+'px'})}}
 function qTabs(){if(ftq)return;ftq=requestAnimationFrame(function(){ftq=0;fitTabs()})}window.fitTabs=qTabs;addEventListener('resize',qTabs);
 if(document.fonts&&document.fonts.ready)document.fonts.ready.then(qTabs);
 window.setLang=function(code){WS('lang',code);var o=$('lcm');if(o)o.remove();return load(code)};
 // Nyelvválasztó menü: az összes nyelv a saját nevén
 var lb=$('bLang');if(lb){lb.onclick=function(e){e.stopPropagation();var o=$('lcm');if(o){var same=o.dataset.k==='l';o.remove();if(same)return}
  o=document.createElement('div');o.id='lcm';o.dataset.k='l';o.className='lng';o.setAttribute('role','menu');
  o.innerHTML='<h4>'+esc(tr('Nyelv'))+'<button type="button" class="lx" aria-label="'+esc(tr('Bezárás'))+'">✕</button></h4><div class="ll">'+I18L.map(function(x){return'<button type="button" class="it lnm'+(x[0]===LANG?' on':'')+'" data-lang="'+x[0]+'" lang="'+x[0]+'" dir="'+x[2]+'">'+esc(x[1])+'</button>'}).join('')+'</div>';
  document.body.appendChild(o);var r=lb.getBoundingClientRect(),fx=innerWidth<=640;o.style.top=(r.bottom+(fx?0:scrollY)+8)+'px';if(fx)o.style.maxHeight=(innerHeight-r.bottom-24)+'px';o.style.left=Math.max(8,Math.min(innerWidth-o.offsetWidth-8,r.right+scrollX-o.offsetWidth))+'px';
  o.onclick=function(ev){if(ev.target.closest('.lx')){o.remove();return}var b=ev.target.closest('[data-lang]');if(b)setLang(b.dataset.lang)}}}
 mo.observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:ATTR});
 var st=LS('lang',null);if(!st){var nl=(navigator.languages||[navigator.language||'hu']).map(function(x){return String(x).toLowerCase()});for(var i=0;i<nl.length;i++){var c=nl[i].split('-')[0];if(nl[i]==='tl'||c==='tl')c='fil';if(c==='no'||c==='nn')c='nb';if(AVAIL[c]){st=c;break}}}
 load(st||'hu')})();
// YouTube lejatszo (ha nem toltheto be, az ikonok sima YouTube-linkek maradnak)
window.onYouTubeIframeAPIReady=function(){ready=true;if(want)want()};
var s=document.createElement('script');s.src='https://www.youtube.com/iframe_api';s.async=true;
s.onerror=function(){ready=false;document.documentElement.classList.add('noyt')};
document.head.appendChild(s);
function mark(){
 document.querySelectorAll('.ic.on').forEach(function(a){a.classList.remove('on');var e=a.querySelector('.eq');if(e)e.remove()});
 if(Q==null||cur<0)return;
 var d0=DATA[Q]&&DATA[Q][cur];if(!d0)return;var li=document.querySelector('#'+(Q==='fav'?'fav':'main')+' li[data-id="'+d0[3]+'"]'),a=li&&li.querySelector('.ic');if(!a)return;
 a.classList.add('on');a.insertAdjacentHTML('beforeend','<span class="eq" aria-hidden="true"><i></i><i></i><i></i></span>');
 document.body.classList.toggle('paused',!playing);
}
function setPP(p){playing=p;$('ppI').setAttribute('d',p?'M4 2h3v12H4zM9 2h3v12H9z':'M4 1.5v13l10-6.5z');$('bPP').setAttribute('aria-label',p?'Szünet':'Lejátszás');mark()}
function play(l,i){
 var d=DATA[l][i];if(!d)return;Q=l;cur=i;
 document.body.classList.add('docked');
 $('mPos').textContent=NAME[l]+' · '+(i+1)+'.'+(ORD?' · keverve':'');$('mT').textContent=d[0];$('mA').textContent=d[1];
 $('live').textContent='Most szól: '+d[0]+', '+d[1];favBtn();
 var x=$('mX');x.hidden=true;
 if(!d[2]){x.hidden=false;x.innerHTML='Ehhez a dalhoz nincs beágyazható videó. <a target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query='+encodeURIComponent(d[1]+' '+d[0])+'">Keresés a YouTube-on</a>';
  if(P&&P.stopVideo)P.stopVideo();setPP(false);return}
 if(!P){P=new YT.Player('yt',{videoId:d[2],playerVars:{autoplay:1,playsinline:1,rel:0},events:{
   onReady:function(e){e.target.playVideo()},
   onStateChange:function(e){if(e.data===1)setPP(true);else if(e.data===2)setPP(false);else if(e.data===0){setPP(false);step(1)}},
   onError:function(){var d=DATA[Q][cur];x.hidden=false;x.innerHTML='Ez a videó csak a YouTube-on játszható le. <a target="_blank" rel="noopener" href="https://www.youtube.com/watch?v='+d[2]+'">Megnyitás</a>';setPP(false)}}});}
 else P.loadVideoById(d[2]);
 setPP(true);
}
function step(n){if(Q==null||/0$/.test(Q))return;if(ORD){var p=pos+n;if(p<0||p>=ORD.length)return;pos=p;play(Q,ORD[p]);return}var j=cur+n;if(j<0||j>=DATA[Q].length)return;play(Q,j)}
function shuffle(l){ORD=DATA[l].map(function(_,i){return i});for(var i=ORD.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=ORD[i];ORD[i]=ORD[j];ORD[j]=t}pos=0;play(l,ORD[0])}
document.addEventListener('click',function(e){
 var a=e.target.closest('.ic')||(false&&e.target.closest('li').querySelector('.ic'));if(!a||!ready||e.metaKey||e.ctrlKey||e.shiftKey)return;
 e.preventDefault();ORD=null;play(a.closest('.grid').dataset.list,+a.dataset.i);
});
$('seq').onclick=function(){ORD=null;if(ready)play(L,0);else{var l=L;want=function(){ORD=null;play(l,0)};if(document.documentElement.classList.contains('noyt'))window.open(document.querySelector('#g-'+L+' .ic').href,'_blank')}};
$('all').onclick=function(){if(ready)shuffle(L);else{var l=L;want=function(){shuffle(l)};if(document.documentElement.classList.contains('noyt')){var as=document.querySelectorAll('#g-'+L+' .ic');window.open(as[Math.floor(Math.random()*as.length)].href,'_blank')}}};
$('bPrev').onclick=function(){step(-1)};$('bNext').onclick=function(){step(1)};
$('bPP').onclick=function(){if(!P||!P.getPlayerState)return;P.getPlayerState()===1?P.pauseVideo():P.playVideo()};
$('bX').onclick=function(){if(P&&P.stopVideo)P.stopVideo();document.body.classList.remove('docked');Q=null;cur=-1;setPP(false)};
// offline / telepitheto (csak valodi tarhelyen)
if('serviceWorker' in navigator&&window.isSecureContext&&window.top===window.self){try{navigator.serviceWorker.register('sw.js').catch(function(){})}catch(e){}}
})();
