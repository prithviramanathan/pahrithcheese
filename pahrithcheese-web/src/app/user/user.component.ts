import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
  email: string;

  constructor(private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
    this.route
      .queryParams
      .subscribe(params => {
        this.email = params.email;
      });
  }

}
