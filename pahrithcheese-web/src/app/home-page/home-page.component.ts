import { Component, OnInit } from '@angular/core';
import { CheeseApiService } from '../services/cheese-api.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  email: string;

  constructor(private cheeseService: CheeseApiService) { }

  ngOnInit() {
  }

  saveUser() {
    this.cheeseService.setEmail(this.email);
  }
}
