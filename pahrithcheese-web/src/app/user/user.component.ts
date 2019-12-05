import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CheeseApiService } from '../services/cheese-api.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  email: string;
  favorites: [string];
  friends: [string];

  constructor(private cheeseService: CheeseApiService, private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
    this.route
      .queryParams
      .subscribe(params => {
        this.email = params.email;
      });

    this.cheeseService.getProfile(this.email).subscribe((data) => {
      this.favorites = data["liked cheeses"];
      this.friends = data["friends"];
    });
  }

}
