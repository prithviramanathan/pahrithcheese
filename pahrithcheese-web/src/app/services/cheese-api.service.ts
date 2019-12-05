import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/x-www-form-urlencoded'
  })
};

@Injectable({
  providedIn: 'root'
})
export class CheeseApiService {
  private email: string;

  constructor(private httpClient: HttpClient) { }

  public getCheese(cheese: string) {
    return this.httpClient.get(`http://3.15.32.200/search?cheeseName=${cheese}`);
  }

  public updatePairing(cheese: string, pair: string) {
    let body = new HttpParams();
    body = body.set('cheeseName', cheese);
    body = body.set('pairing', pair);
    return this.httpClient.post(`http://3.15.32.200/update-pairings`, body, httpOptions);
  }

  public setEmail(email: string) {
    this.email = email;
  }

  public getEmail() {
    return this.email;
  }
}
