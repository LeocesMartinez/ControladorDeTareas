import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, ObservableInput } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://127.0.0.1:5000'; // Cambia por la URL de tu API

  constructor(private http: HttpClient) {   }

  // Método para obtener todos los elementos
  getAll<T>(resource: string, queryParams?: any): Observable<T[]> {

    var url = `${this.apiUrl}/${resource}`

    if (queryParams) {
      url += '?' + this.serializeParams(queryParams);
    }
    return this.http.get<T[]>(url)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Método para obtener un elemento por su ID
  getById<T>(resource: string, id: any): Observable<T> {
    return this.http.get<T>(`${this.apiUrl}/${resource}/${id}`)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Método para crear un nuevo elemento
  create<T>(resource: string, item: any): Observable<T> {
    const headers = new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded');

    const body = new URLSearchParams();
    for (const key in item) {
      if (item.hasOwnProperty(key)) {
        body.set(key, item[key]);
      }
    }

    console.log('Parametros POST', item)
    return this.http.post<T>(`${this.apiUrl}/${resource}`, body.toString(), {headers: headers})
      .pipe(
        catchError(this.handleError)
      );
  }

  // Método para actualizar un elemento existente
  update<T>(resource: string, item: any): Observable<T> {
    const headers = new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded');
    
    const body = new URLSearchParams();
    for (const key in item) {
      if (item.hasOwnProperty(key)) {
        body.set(key, item[key]);
      }
    }
    return this.http.put<T>(`${this.apiUrl}/${resource}`, body.toString(), {headers: headers})
      .pipe(
        catchError(this.handleError)
      );
  }

  // Método para eliminar un elemento
  delete<T>(resource: string, item: any): Observable<T> {
    const headers = new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded');
    
    const body = new URLSearchParams();
    for (const key in item) {
      if (item.hasOwnProperty(key)) {
        body.set(key, item[key]);
      }
    }

    return this.http.delete<T>(`${this.apiUrl}/${resource}`, {headers: headers, body: body.toString()})
      .pipe(
        catchError(this.handleError)
      );
  }

  // Método privado para manejar errores
  private handleError(error: any, c: Observable<any>): ObservableInput<any>{
    console.error('Ocurrió un error:', error);
    throw error;
  }

  // Método para serializar los parámetros de consulta
  private serializeParams(params: any): string {
    return Object.keys(params).map(key => `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`).join('&');
  }
}