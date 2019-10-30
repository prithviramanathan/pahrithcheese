import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CheeseApiService {

  constructor(private httpClient: HttpClient) { }

  public getCheese(cheese: string){
    return this.httpClient.get(`http://3.15.32.200/search?cheeseName=${cheese}`)
  }
}
