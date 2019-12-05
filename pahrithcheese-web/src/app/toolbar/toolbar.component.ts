import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CheeseApiService } from '../services/cheese-api.service';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss']
})
export class ToolbarComponent implements OnInit {

  constructor(private route: ActivatedRoute, private router: Router, private cheeseService: CheeseApiService) { }

  ngOnInit() {
  }

  goToUser() {
    this.router.navigate(['/user'], { queryParams: { email: this.cheeseService.getEmail() } });
  }

}
