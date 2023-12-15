class Solution {
  function destCity($paths) {
      $destinations = array();
  
      foreach ($paths as $p) {
          $destinations[$p[0]] = $p[1];
      }
  
      $currentCity = $paths[0][1];
  
      while (array_key_exists($currentCity, $destinations)) {
          $currentCity = $destinations[$currentCity];
      }
  
      return $currentCity;
  }
}
