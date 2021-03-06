import { combineReducers } from 'redux';

import { authentication } from './authentication.reducer';
import { registration } from './registration.reducer';
import { users } from './users.reducer';
import { alert } from './alert.reducer';
import { hist } from './history.reducer';
import { full } from './full.reducer';
import { images } from './images.reducer';

const rootReducer = combineReducers({
  authentication,
  registration,
  users,
  alert,
  hist,
  full,
  images
});

export default rootReducer;
