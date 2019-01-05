// NOTE: Travis installs libboost test version 1.5.4
//#define BOOST_TEST_DYN_LINK

#define BOOST_TEST_MODULE "lid_toolkitAPI"
#include "test_lid_toolkitapi.hpp"

using namespace std;

// Custom test to check the minimum number of correct decimal digits between
// the test and the ref vectors.
boost::test_tools::predicate_result check_cdd(std::vector<double>& test,
    std::vector<double>& ref, long cdd_tol)
{
    double tmp, min_cdd = 10.0;

    // TODO: What if the vectors aren't the same length?

    std::vector<double>::iterator test_it;
    std::vector<double>::iterator ref_it;

    for (test_it = test.begin(); test_it < test.end(); ++test_it) {
        for (ref_it = ref.begin(); ref_it < ref.end(); ++ref_it) {

             if (*test_it != *ref_it) {
                // Compute log absolute error
                tmp = abs(*test_it - *ref_it);
                if (tmp < 1.0e-7)
                    tmp = 1.0e-7;

                else if (tmp > 2.0)
                    tmp = 1.0;

                tmp = - log10(tmp);
                if (tmp < 0.0)
                    tmp = 0.0;

                if (tmp < min_cdd)
                    min_cdd = tmp;
            }
        }
    }

    return floor(min_cdd) <= cdd_tol;
}

// Non-Fixuture Unit Tests
BOOST_AUTO_TEST_SUITE(test_lid_toolkitapi)

// Test Model Not Open
BOOST_AUTO_TEST_CASE(model_not_open) {
    
    int error;
    int int_val=0;
    
    //Lid Unit
    error = swmm_getLidUCount(0, &int_val);
    BOOST_CHECK_EQUAL(error, ERR_API_INPUTNOTOPEN);
}

BOOST_AUTO_TEST_SUITE_END()
/*

BOOST_AUTO_TEST_SUITE(test_lid_toolkitapi_fixture)

// Testing for Simulation Started Error
BOOST_FIXTURE_TEST_CASE(sim_started_check, FixtureBeforeStep) {

}


// Testing for invalid object index
BOOST_FIXTURE_TEST_CASE(object_bounds_check, FixtureOpenClose) {

}


// Testing for invalid parameter key
BOOST_FIXTURE_TEST_CASE(key_bounds_check, FixtureOpenClose) {

}


// Testing for Project Settings after Open
BOOST_FIXTURE_TEST_CASE(project_info, FixtureOpenClose){

}


// Testing for subcatchment get/set
BOOST_FIXTURE_TEST_CASE(getset_subcatch, FixtureOpenClose) {

}


// Testing for node get/set
BOOST_FIXTURE_TEST_CASE(getset_node, FixtureOpenClose) {

}


// Testing for link get/set
BOOST_FIXTURE_TEST_CASE(getset_link, FixtureOpenClose) {

}


// Testing for After Start Errors
BOOST_FIXTURE_TEST_CASE(sim_after_start_check, FixtureBeforeStep){

}


// Testing Results Getters (During Simulation)
BOOST_FIXTURE_TEST_CASE(get_result_during_sim, FixtureBeforeStep){

}


// Testing Results Getters (Before End Simulation)
BOOST_FIXTURE_TEST_CASE(get_results_after_sim, FixtureBeforeEnd){

}

BOOST_AUTO_TEST_SUITE_END()
*/