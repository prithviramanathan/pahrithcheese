import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CheeseApiService } from '../services/cheese-api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  email: string;
  favorites: [string];
  friends: [string];
  userEmail: string;
  addEmail: string;

  constructor(private cheeseService: CheeseApiService, private route: ActivatedRoute, private router: Router, private toastrService: ToastrService) { }

  ngOnInit() {
    this.route
      .queryParams
      .subscribe(params => {
        this.email = params.email;
      });

    this.userEmail = this.cheeseService.getEmail();

    this.getProfile();
  }

  goToUser(friend: string) {
    this.router.navigate(['/user'], { queryParams: { email: friend } });
    this.route
      .queryParams
      .subscribe(params => {
        this.email = params.email;
        console.log(this.email);
        this.getProfile();
      });
  }

  getProfile() {
    this.cheeseService.getProfile(this.email).subscribe((data) => {
      this.favorites = data["liked cheeses"];
      this.friends = data["friends"];
    });
  }

  toggleFriend() {
    console.log('toggle friend');
    this.cheeseService.toggleFriend(this.userEmail, this.addEmail).subscribe((data) => {
      console.log(data);
      if(data[0] === 'removed friend') {
        this.toastrService.warning('Removed friend!');
      }
      else if (data[0] === 'liked the cheese') {
        this.toastrService.success('Added friend!');
      }

      this.getProfile();
      console.log(this.friends);
    });
  }

}
