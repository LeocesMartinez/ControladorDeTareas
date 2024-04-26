/*import { Component } from '@angular/core';

@Component({
  selector: 'app-bienvenida',
  templateUrl: './bienvenida.component.html',
  styleUrl: './bienvenida.component.css'
})
export class BienvenidaComponent {

  cerrarSesion() {
    localStorage.setItem('usuario', '');
  }  
}
*/
import { Component } from '@angular/core';
import { Router } from '@angular/router';
 
@Component({
  selector: 'app-bienvenida',
  templateUrl: './bienvenida.component.html',
  styleUrls: ['./bienvenida.component.css']
})
export class BienvenidaComponent {
  constructor(private router: Router) {}
  /*cerrarSesion() {
    localStorage.removeItem('usuario');
  }  */
}