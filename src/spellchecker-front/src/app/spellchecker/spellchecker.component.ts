import { Component, OnInit } from '@angular/core';
import {SpellcheckerService} from 'src/app/spellchecker.service'
import { FormControl} from '@angular/forms';
import { Text } from '../models/text';
import { Request } from '../models/request';

@Component({
  selector: 'app-spellchecker',
  templateUrl: './spellchecker.component.html',
  styleUrls: ['./spellchecker.component.scss']
})
export class SpellcheckerComponent implements OnInit {
  text = new FormControl('')
  public showSpinner = false;
  public showHistory = false;
  public history : Request[] = [];
  constructor(private spellcheckerService: SpellcheckerService) {

  }

  ngOnInit(): void {
   this.spellcheckerService.getRequestHistory().subscribe((history: Request[]) => {
      this.history = history
    })
  }

  spellcheck(): void{
    this.showSpinner = true;
    this.spellcheckerService.spellCheck(this.text.value).subscribe((data: Text) =>{
      this.showSpinner = false;
      this.text.setValue(data.text);
      this.requestHistory();
    })
  }

  requestHistory(): void{
    this.showSpinner = true;
    this.spellcheckerService.getRequestHistory().subscribe((history: Request[]) => {
      this.showSpinner = false;
      this.history = history;
    })
  }
}
