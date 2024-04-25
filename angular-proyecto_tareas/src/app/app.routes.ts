import { Routes } from '@angular/router';
import { BienvenidaComponent } from './bienvenida/bienvenida.component';
import { TareasComponent } from './tareas/tareas.component';

export const routes: Routes = [
    {path : '', component : BienvenidaComponent},
    {path: 'usuario', loadChildren:() => import('./usuario/usuario.module').then(mod => mod.UsuarioModule)},
    { path: 'tareas', component: TareasComponent}
];
