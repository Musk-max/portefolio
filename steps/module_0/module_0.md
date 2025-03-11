# File and folder structures
Ce document est en quelque sorte un ensemble de fleet notes ou on a le code d'abord 
et une petite explication en suite
# liens
cdn , et css en haut  scripts en bas , 

Le pseudo-élément ::selection permet d'appliquer des règles CSS à une portion du document qui a été sélectionnée par l'utilisateur (via la souris ou un autre dispositif de pointage).

Le pseudo-élément ::-webkit-scrollbar permet de modifier le style de la barre de défilement associée à un élément. Il s'agit d'un pseudo-élément propriétaire, uniquement disponible pour les navigateurs WebKit.

::-webkit-scrollbar-track — la piste (la zone de progression) de la barre de défilement

::-webkit-scrollbar-thumb — l'emplacement qui permet de déplacer la barre de défilement.

La propriété CSS overflow est une propriété raccourcie qui définit comment gérer le dépassement du contenu d'un élément dans son bloc. Elle définit les valeurs des propriétés overflow-x et overflow-y.
 body{
        overflow: hidden;
      }

La propriété transition est une propriété raccourcie pour les propriétés transition-property, transition-duration, transition-timing-function et transition-delay.

Elle permet de définir la transition entre deux états d'un élément. Les différents états peuvent être définis à l'aide de pseudo-classes telles que :hover ou :active ou être définis dynamiquement avec JavaScript.

# Fin de la partie configuration globale

La propriété border-right est une propriété raccourcie qui permet de décrire la bordure droite d'un élément.

La propriété CSS flex-flow est une propriété raccourcie pour les propriétés flex-direction et flex-wrap.

  text-transform: uppercase;
  met l'élemment sélectionné en majuscule

  La propriété border-bottom est une propriété raccourcie qui définit la bordure du côté bas d'un élément.

C'est une propriété raccourcie qui synthétise :

border-bottom-width,
border-bottom-color,
border-bottom-style.
Ces propriétés permettent de décrire la bordure du côté bas d'un élément.

La propriété CSS font-weight permet de définir la graisse utilisée pour le texte. Les niveaux de graisse disponibles dépendent de la police (cf. font-family). Certaines fontes n'existent qu'avec les niveaux de graisses normal et bold.

 display:block; (voir flower doc)

  .header .navbar  a.active,
      .header .navbar  a:hover{
        background-color: var(--yellow);
      } pour survoler les a et les mettres en jaune

      La pseudo-classe :active permet de cibler un élément lorsque celui-ci est activé par l'utilisateur. Elle permet de fournir un feedback indiquant que l'activation a bien été détectée par le navigateur. Lorsqu'on a une interaction avec un pointeur, il s'agit généralement du moment entre l'appui sur le pointeur et le relâchement de celui-ci.

      La mise en forme associée peut être surchargée par les autres pseudo-classes pour les liens : :link, :hover et :visited lorsqu'elles sont utilisées dans des règles qui suivent. Afin de mettre en forme les liens de façon correcte, la règle avec :active doit être écrite après les autres : :link — :visited — :hover — :active.

        .header .follow a{
        background-color: var(--yellow);
        font-size: 3rem;
        margin:0 1rem;
        cursor: pointer;
      }ce sont les règles commune pour les logos de réseaux 

        .header .follow a:hover{
        transform: rotate(360deg);
        transition:.2s linear !important;
      }ajouter un effet de rotation dès qu'on survole les logos de réseaux 
      Les transitions c'est pour les hover-flow ou autres effets pour gérer leur affichage en forme 

      Quelle règle a fait passer la navbar à gauche ?

      Cette fois ci le menu bouton n'est plus un label connecter a une checkbox afin de détecter les variations de l'écran : commence avec une div car ce menu doit exister 
      qu'il y ait responsivité ou pas car il fait partie de la logique de notre application 

        <div id="menu-button" class="fas fa-bars"></div>
        
      #menu-button{
        position:absolute;
        top:0;right:-5.5rem;
        height:4.5rem;
        line-height:4.5rem;
        width: 5rem;
        font-size: 2.5rem;
        background-color: #333;
        cursor: pointer;
        color:var(--blanc);


      } ajout du menu bouton au début dans le header pour qu'il soit bien en haut
      Redimensionnement, style et définition de son comportement ensuite

      let menu = document.querySelector("#menu-button");
let header = document.querySelector(".header");


menu.onClick = ()=>{
    div.classList.toggle('fa-times'); 
    header.classList.toggle('active'); 
    document.body.classList.toggle('active'); 

};

window.onscroll = ()=>{
    if(window.innerWidth < 991){
        div.classList.remove('fa-times'); 
        header.classList.remove('active'); 
        document.body.classList.remove('active'); 

    }
};variables et methodes javascript qui contiennent les comportements qu'on execute au clique et au scroll
Faison les effets css associés à ses comportements

Les borders là servent à souligner les choses: border-bold...

Faire un fichier avec l'équivalent des règles et des effets en figma et en css

menu.addEventListener("click",  () =>{
    menu.classList.toggle('fa-times'); 
    header.classList.toggle('active'); 
    document.body.classList.toggle('active'); 
}
);

window.addEventListener("scroll",  () =>{
    if(window.innerWidth < 991){
        menu.classList.remove('fa-times'); 
        header.classList.remove('active');
        document.body.classList.remove('active');
    } 
}
);

Finalement ce sont ces deux blocs qui sont les deux bonnes syntaxes javaScript , 
c'est a cause de ca mon bouton menu-button ne fonnctionnait plus là 

Plutard utiliser ce meme principe ou je mets quelque chose à -35 rem juste pour le cacher quelque chose et quand on clique sur un bouton il fvient à +35 rem et se déploie pour 
cacher des choses sur un site souvent mme dans le footer . et si je suis méchant faire
mettre le hamburger button transparent, je peux aussi faire un site web avec des tiroirs 
c'est à dire les trucs trop superflus la les cacher avec ce mm principe .Oubien par exemple un jeu ou il y a plusieurs cases et mais une seule qui contient des bénéfices pour mes clients ( les jeux marketings là ). Celui qui trouve la bonne case gagne. 
Organiser des évènements aussi, des thématiques ... l'art de la bonne com

.header .navbar {
        width: 100%;
           }
  .header.active{
       left: 0;
     }
     body.active{
        padding-left: 35rem;
      }
.header{
        position: fixed;
        top:0;left:-35rem;}
        et aussi là dans le header le left est passé de 0 à -35 rem pour le faire disparaitre de la vue du user 
           appliquer ca aussi dans le process de sidebar hamburger


///////////////////////////////////////////////Le header est fini ici :

<section class="home" id="home">
        <div class="image">
                <img src="images/img_profile.jpg" alt="">
        </div>
        <div class="content">
            <h3>Hi, I AM FRANCK LAGOU !</h3>
            <span>Développeur full stack </span>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus consectetur 
                blanditiis error iure dolore sed porro reprehenderit odit officia voluptate. 
                Explicabo reprehenderit nam, maiores qui ab suscipit animi voluptates porro.</p>
            <a href="#about" class="btn"></a>
        </div>

</section> contenu de la section home à ajouter dans le html , si cetait un autre modèle 
home aurait sa vue tandis que header et footer et certains éléments comments seraient hérités par toutes les pages 

Maintenant user(Franck LAGOU) serait un objet (nom, image, fonction, text, comme atribut)

section{
        padding:3rem 2rem;
        margin: 0 auto;
        max-width: 1200px;
        text-align: center;
      } Les conditions communes pour toutes les elements section en général 

 .home{
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap:2rem;
      } et les conditions spécifiques aux élément de la classe au home (section home)

      .home .image img{
        height: 65rem;
        padding:2rem;
        border: var(--border-bold);
      } redimensionemnt des de l'image et ajout de bordure marron autour

       .home .content{
       flex:1 1 40rem;
      }  repositionement de content le text par rapport à l'image vu que le tout 
      est en mode flex depuis toute la section home on utilise les propriété de flex
      pour aligner les blocs

       .home .content h3{
          text-transform: uppercase; 
          font-size: 5rem;
          margin-bottom:.5rem;     
      }  Mise en forme du titre du contenu uniquement, le paragraphe vient en bas

      .home .content span{
            display: inline-block; 
            padding: 1 2rem;
            background-color: var(--yellow);
            font-size:2.5rem;
            margin:1rem 0;
          } dans un texte quand on veut mettre en lumière ou en relief un élément précis 
          exemple, le surligner, lui donner une coleur particulière par rapport au reste
          du texte ou du paragraphe on le met dans un span. 
          eT LA Maintenant donc le mot clé qui est ma fonction: developper full sctack doit 
          etre sur ligné sur la plate forme. 

          Donc chaque séance on prend la maquette on y liste les éléments sur une feuille 
          puis on se demande quelle règle appliquer à chaque élément en équipe ou en solo 
          pour que ca ressemble a la maquette; FAIRE DES ESSAIS et des recherches sur la catégorie ou la nature de l'élément( animation, marge, surligné..) ET LORSQUE Ca marcHE bien notér ca quelque part et associer à la maquette pour pouvoir utiliser comme template plutard de la correspondance css figma...

           .home .content P{
            font-size:1.7rem;
            line-height: 2;
            padding: 1rem 0;
          } la taille, la hauteur de ligne et les innerspace entre les textes

          Et quand j'ai un front à creer ouvrir mes anciens modules et voir quelles sont 
          les règles que j'ai déjai les ressencées tout d'un coup à partir du catalogue de règles
          et de leur signification qui ont été appliquées au module . et ensuite rechercher celles qui manquent 

          On front tout ce qui est appel à l'action en général quand tu le survole, il 
          doit y avoir un effet (exemple un bouton qui ouvre un lien le bouckground peut changer du blanc au noir par exemple)

               .btn{
            display: inline-block;
            margin-top:1rem;
            cursor:pointer;
            padding: 1rem 3rem;
            border:var(--border-light);
            font-size: 2rem;
          }
          .btn:hover{
            background-color: var(--vert);
            color: var(--blanc);
          }
          Maintenant là ajoutons le style du bouton about me qui redirige vers la page du 
          meme nom. 
          On le met en inline-block comme ca tout ses elements sont bien alignés aucun de va a la ligne dans le bouton. Puis les règles communes et après ajouter un effet de survol c'est à dire quand il est sur voler changer le background color et le color pour créer un contrast agréable à l'utilisateur et pour sortir de la monotonie du site.

            min-height: 100vh; ajouter cette regle la a tout ce qui s"applique globalement
            dans le home, peut etre c'est pour garantir une hauteur de 100vh de notre section
            en cas de réduction décran

             .home .image img{
        height: auto;
         width: 100%;
      } AJOUTER CES regles juste en dessous du mm bloc précédent est qu'il y aura conflit 
      entre les heights je sais pas , a mon avis c pour que l'image s'adapte automatiquement
      en cas de changement et si ya pas changement c'est le height explicite qui sera exécuté
      et je pense que c'est a cause de ses deux la qu'on a créer deux blocs de meme noms 
      .En faire cas détudes on crée deux blocs de mm noms pour éviter qu'un bloc contienne deux fois la mm regle (avec et sans responsivité)

      Autant pour moi c'est juste que celle ci sera dans le bloc @media de 450px;