# 📊 데이터 명세서: Airbnb

데이터 설명 : 2025/3/2 뉴욕시의 에어비엔비 숙소 정보

데이터 차원 : (22308, 72)

| Column Name | Data Type | Description | Preprocessing / Notes |
| :--- | :--- | :--- | :--- |
| `id` | integer | 숙소 unique id | Primary Key |
| `source` | string | 출처 | 단일 값으로 제거 |
| `name` | string | 숙소 이름 | NLP / 관련 숙소 가격에 영향을 미치는 주요 단어 추출(우선순위 낮음) |
| `description` | string | 숙소 설명 | NLP / 설명 길이가 길수록 신뢰성이 있는가(방문 수 관련, 우선순위 낮음) |
| `neighborhood_overview` | string | 숙소 동네 설명 |  |
| `host_id` | integer | 호스트 id | 숙소 개수와 가격/방문 수의 상관관계? |
| `host_since` | string | 호스트 가입일 | datetime 변환 필요 |
| `host_location` | string | 호스트 거주지 | NY ,New York 등 동일해보이는 것 어떻게 처리할지 |
| `host_about` | string | 호스트 설명(본인) | 이진 or 길이 처리, 신뢰성 |
| `host_response_time` | string | 호스트 응답 시간(hour, few hours, day) | 이것도 신뢰성...인 것 같음 |
| `host_response_rate` | string | 호스트 응답률 | 99%와 같이 기록. 99나 0.99로 전처리 필요 |
| `host_acceptance_rate` | string | 호스트 예약 수락률 | 99%와 같이 기록. 99나 0.99로 전처리 필요 |
| `host_is_superhost` | string | 슈퍼호스트 여부 | (t/f) True/False로 전처리 필요 |
| `host_neighbourhood` | string | 호스트 동네 | host_location보다 더 작은 단위의 정보 |
| **`host_listings_count`** | float | 에어비앤비 사이트에 노출되는 호스트의 숙소 개수 | 개인/전문 업체(10개 이상)에 따른 가격 차이? |
| `host_total_listings_count` | float | 에어비앤비에 등록된 호스트의 숙소 개수 (비노출 포함) | 99.91%가 위의 칼럼보다 크거나 같음 |
| `host_verifications` | list | 호스트 신원 인증 방식 | ['email', 'phone', 'work_email']과 같이 리스트로 되어있어, 원-핫 인코딩, 혹은 개수 처리 필요 |
| `host_has_profile_pic` | string | 호스트 본인 사진 등록 여부 | (t/f) True/False로 전처리 필요 |
| `host_identity_verified` | string | 실제 신원 확인 여부 | (t/f) True/False로 전처리 필요 |
| `neighbourhood` | string | ? | 해석 애매, 제거해야 할 듯 |
| `neighbourhood_cleansed` | string | 동네 지역 | group보다 더 세부적인 정보 |
| `neighbourhood_group_cleansed` | string | 지역 정보 | Manhattan, Brooklyn, Queens, Bronx, Staten Island 5가지 |
| `latitude` | float | 숙소 위치 위도 | 위,경도로 숙소 위치와 가격 시각화|
| `longitude` | float | 숙소 위치 경도 | 위,경도로 숙소 위치와 가격 시각화|
| `property_type` | string | 숙소 유형 | 유형 전처리 묶는 과정 필요 |
| `room_type` | string | 방 유형 | **룸 타입에 따른 가격의 차이 확인 필요** |
| `accommodates` | int | 최대 수용 인원 | **가격과 관련 있을 듯** |
| `bathrooms` | float | 욕실 개수 | 1.5, 2.5와 같이 소수점 해석 필요 |
| `bathrooms_text` | string | 화장실 세부 설명 | bathrooms과 어느 정도 겹침, 협의 필요 |
| `bedrooms` | float | 침실 개수 | **가격의 차이 확인 필요** |
| `beds` | float | 침대 개수 | **가격의 차이 확인 필요** |
| `amenities` | string | 편의 시설 | **원-핫 인코딩 or 개수로 전처리 필요** |
| `price` | string | 가격 | **종속변수**, **'$', ','** 전처리 필요|
| `minimum_nights` | integer | 최소 숙박 일수 | 이 숙소에 묵으려면 최소 몇 박 이상 예약해야 하는가 |
| `maximum_nights` | integer | 최대 숙박 일수 | 이 숙소에서 최대 몇 박 이상 예약할 수 있는가 |
| `minimum_minimum_nights` | float | 1년 중 가장 짧게 설정된 최소 숙박 일수 | - |
| `maximum_minimum_nights` | float | 1년 중 가장 길게 설정된 최소 숙박 일수 | 예: 크리스마스 연휴엔 무조건 4박 이상 |
| `minimum_maximum_nights` | float | 1년 중 가장 짧게 설정된 최대 숙박 일수 | - |
| `maximum_maximum_nights` | float | 1년 중 가장 길게 설정된 최대 숙박 일수 | - |
| `minimum_nights_avg_ntm` | float | 향후 1년 동안 적용될 평균 최소 숙박 일수 | - |
| `maximum_nights_avg_ntm` | float | 향후 1년 동안 적용될 평균 최대 숙박 일수 | - |
| `calender_updated` | float | - | 전체 결측치. 제거해야 함 |
| `has_availability` | str | 현재 예약 가능 상태 | (t/f) True/False로 전처리 필요 |
| `availability_day` | integer | 향후 day일 중 예약 가능 일수 | 숫자가 작을 수록 인기가 많다는 뜻일 듯 |
| `availability_eoy` | integer | 현재 시점부터 12/31까지의 예약 가능 일수 | 숫자가 작을 수록 인기가 많다는 뜻일 듯 |
| `calendar_last_scraped` | string | 스크랩 시점 | 제거 필요 |
| `number_of_reviews` | integer | 리뷰 개수 | 리뷰 개수도 신뢰도...이지만 가격과 관련이 있을까? |
| `number_of_reviews_ltm` | integer | 리뷰 개수(지난 1년 간) | 리뷰 개수도 신뢰도...이지만 가격과 관련이 있을까? |
| `number_of_reviews_l30d` | integer | 리뷰 개수(지난 30일간) | 리뷰 개수도 신뢰도...이지만 가격과 관련이 있을까? |
| `number_of_reviews_ly` | integer | 리뷰 개수(지난 1년간) | ltm 변수와 17000개 가량이 같음. |
| **`estimated_occupancy_l365d`** | integer | 지난 1년간의 추정 점유율 | 최근 1년간 리뷰 수(number_of_reviews_ltm) × 리뷰 작성 확률 × 평균 숙박 일수 |
| **`estimated_revenue_l365d`** | float | 지난 1년간의 추정 매출액 | price (숙박비) × estimated_nights_booked_l365d (추정 예약 숙박일 수) |
| `first_review` | string | 첫 리뷰 일자 |  |
| `last_review` | string | 마지막 리뷰 일자 |  |
| **`review_scores_rating`** | float | 리뷰 총 평균 |  |
| **`review_scores_accuracy`** | float | 숙소 일치성 평점 | 사진이나 설명이 실제와 얼마나 똑같았나? (허위 매물 판별) |
| **`review_scores_cleanliness`** | float | 청결도 |  |
| **`review_scores_checkin`** | float | 체크인 편의성 |  |
| **`review_scores_communication`** | float | 호스트 소통 능력 |  |
| **`review_scores_location`** | float | 숙소 위치 만족도 |  |
| **`review_scores_value`** | float | 가격에 대한 만족도 |  |
| **`license`** | string | 숙소 라이센스 | OSE, Exempt, other 등 어떻게 전처리할지? + NaN은 아마 라이센스가 없다는 의미일 듯 |
| `instant_bookable` | string | 게스트가 호스트가 예약 요청을 수락할 필요 없이 자동으로 예약할 수 있는지 여부 | (t/f) True/False로 전처리 필요 |
| `calculated_host_listings_count` | integer | 실제 중복을 제외한 호스트의 숙소 개수 | - |
|`calculated_host_listings_count_entire_homes` | integer | 독채/아파트 개수 | - |
|`calculated_host_listings_count_private_rooms` | integer | 개인실 개수 | 거실/화장실 공유 |
|`calculated_host_listings_count_shared_rooms` | integer | 다인실 개수 | 게스트하우스 |