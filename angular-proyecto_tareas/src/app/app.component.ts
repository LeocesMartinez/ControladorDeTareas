import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {

  title = 'angular-proyecto';
  usuario: string | null = "";

  ngOnInit(): void {
    this.usuario = localStorage.getItem('usuario');
    console.log('usuario', this.usuario);
  }

  cerrarSesion() {
    localStorage.removeItem('usuario');
    this.usuario = '';
  }
}
