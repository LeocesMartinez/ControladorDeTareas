import { Routes } from '@angular/router';
import { BienvenidaComponent } from './bienvenida/bienvenida.component';

export const routes: Routes = [
    {path : '', component : BienvenidaComponent},
    {path: 'usuario', loadChildren:() => import('./usuario/usuario.module').then(mod => mod.UsuarioModule)},
    { path: 'tareas', loadChildren:() => import('./tasks/tasks.module').then(mod => mod.TasksModule)}
];
