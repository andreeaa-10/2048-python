<h1>
    2048
</h1>
Am dezvoltat un joc captivant 2048 în Python, utilizând Kivy pentru a implementa o interfață grafică prietenoasă care îmbunătățește experiența jucătorului. Am creat algoritmi pentru a gestiona mecanica jocului, inclusiv combinarea pieselor și calcularea scorului, asigurând o experiență de joc receptivă și provocatoare. Am integrat funcționalități precum "undo" (revenire), "resume" (reluare) și condiții de terminare a jocului.
<br> </br>
<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img.png">
</p>

<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img_1.png">
</p>

<h3>
    Regulile jocului
</h3>
2048 se joacă pe o grilă de 4×4, care conține piese numerotate ce se mișcă fluid atunci când sunt direcționate cu ajutorul săgeților. De fiecare dată când piesele sunt mutate, o piesă nouă apare aleatoriu într-unul dintre spațiile libere de pe tablă. Piesele se deplasează cât de mult posibil în direcția aleasă, oprindu-se doar atunci când se ciocnesc cu o altă piesă sau ajung la marginea grilei. Dacă două piese cu aceeași valoare se ciocnesc în timpul unei mișcări, acestea se combină într-o singură piesă cu o valoare egală cu suma celor două. Această piesă combinată nu poate fi combinată cu o altă piesă în aceeași mișcare.
<p align="center">
    <img width="300" height="500" src="https://github.com/andreeaa-10/2048-python/blob/main/pictures/img_2.png">
</p>

Am implementat caracteristici specifice în joc, cum ar fi o funcție de reluare care permite jucătorului să continue de unde a rămas și un sistem de mișcare automată care se activează după o perioadă de inactivitate, selectând cea mai bună mișcare posibilă. Jocul este câștigat atunci când se creează o piesă cu valoarea 2048. Pierzi atunci când nu mai sunt posibile mișcări valide, adică atunci când nicio piesă nu poate fi combinată sau mutată.
