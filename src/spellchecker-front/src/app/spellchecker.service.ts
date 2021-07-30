import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import {Text} from 'src/app/models/text'

@Injectable({
  providedIn: 'root'
})
export class SpellcheckerService {
  apiUrl: string = 'http://localhost:3000/dev';
  headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
  constructor(private http: HttpClient) { }

  spellCheck(text: string): Observable<any> {
    let API_URL = `${this.apiUrl}/spellcheck`;
    return this.http.post(API_URL, new Text(text), { headers: this.headers })
      .pipe(
        catchError(this.error)
        )
  }

  getRequestHistory(): Observable<any>{
    let API_URL = `${this.apiUrl}/request_history`;
    return this.http.get(API_URL)
    .pipe(
      catchError(this.error)
      )
  }

  error(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      errorMessage = error.error.message;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }
}
